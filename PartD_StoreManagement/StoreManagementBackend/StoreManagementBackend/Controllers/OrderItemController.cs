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
            if(orderItem.Quantity < 50) {
                return NotFound(new { message = $"Quantity mast be above {orderItem.Quantity}." });
            }

            var product = await _context.Products.FindAsync(orderItem.ProductId);
            if (product == null) { 
                return NotFound(new { message = $"Product with ID {orderItem.ProductId} not found." });
            }

            product.InStock -= orderItem.Quantity;
            _context.OrderItems.Add(orderItem);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetOrderItems", new { orderItem.Id }, orderItem);
        }
    }
}
