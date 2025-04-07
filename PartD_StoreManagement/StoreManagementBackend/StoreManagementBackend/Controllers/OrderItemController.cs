using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using StoreManagementBackend.Models;

namespace StoreManagementBackend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class OrderItemController : ControllerBase {
        private readonly StoreManagementDbContext _context;

        public OrderItemController(StoreManagementDbContext context) {
            _context = context;
        }

        //get orderItem
        [HttpGet]
        public async Task<ActionResult<IEnumerable<OrderItem>>> GetOrderItems() {
            return await _context.OrderItems.ToListAsync();
        }

        //post orderItem
        [HttpPost]
        public async Task<ActionResult<OrderItem>> PostOrderItem([FromBody] OrderItem orderItem) {
            _context.OrderItems.Add(orderItem);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetOrderItems", new { orderItem.Id }, orderItem);
        }
    }
}
