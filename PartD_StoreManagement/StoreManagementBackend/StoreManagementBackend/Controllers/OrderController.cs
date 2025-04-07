using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using StoreManagementBackend.Models;
using StoreManagementBackend.Controllers;

namespace StoreManagementBackend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class OrderController : ControllerBase {
        private readonly StoreManagementDbContext _context;

        public OrderController(StoreManagementDbContext context) {
            _context = context;
        }

        //get all orders
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Order>>> GetOrders() {
            return await _context.Orders.ToListAsync();
        }

        //post order
        [HttpPost]
        public async Task<ActionResult<Order>> PostOrder([FromBody] Order order) {
            order.Supplier = await _context.Users.FirstOrDefaultAsync(u => u.Id == order.SupplierId && u.Role == Role.Supplier);
            _context.Orders.Add(order);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetOrders", new { order.Id }, order);
        }

        //post order status
        [HttpPost("UpdateStatus/{id}")]
        public async Task<ActionResult<Order>> PostOrderStatus(int id, [FromBody] Status status) {
            var order = await _context.Orders.FindAsync(id);
            if (order == null) {
                return NotFound(new { message = $"Order with ID {id} not found." });
            }

            var current = order.Status;

            if (status == Status.Invited) {
                return BadRequest(new { message = "Cannot revert order status to 'Invited'." });
            }

            if (current == Status.Completed) {
                return BadRequest(new { message = "Cannot update a completed order." });
            }

            if ((current == Status.Approval || current == Status.Completed) && status == Status.Approval) {
                return BadRequest(new { message = "Cannot revert order status to 'Approval'." });
            }

            if (current == Status.Invited && status == Status.Completed)
            {
                return BadRequest(new { message = "Cannot revert order status from 'Invited' to 'Completed'." });
            }

            order.Status = status;

            if (status == Status.Approval)
                order.ApprovalDate = DateTime.Now;
            else if (status == Status.Completed)
                order.CompleteDate = DateTime.Now;

            await _context.SaveChangesAsync();

            return Ok(new { message = $"Order {id} updated to status '{status}'." });
        }
    }
}
