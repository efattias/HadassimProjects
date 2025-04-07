using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using StoreManagementBackend.Models;

namespace StoreManagementBackend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductController : ControllerBase {
        private readonly StoreManagementDbContext _context;

        public ProductController(StoreManagementDbContext context) {
            _context = context;
        }

        //get product
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Product>>> GetProducts() {
            return await _context.Products.ToListAsync();
        }

        //post product
        [HttpPost]
        public async Task<ActionResult<Product>> PostProduct([FromBody] Product product) {
            product.Supplier = await _context.Users.FirstOrDefaultAsync(u => u.Id == product.SupplierId && u.Role == Role.Supplier);
            _context.Products.Add(product);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetProducts", new { product.Id }, product);
        }

        //post product
        [HttpPost("UpdateInStock/{id}")]
        public async Task<ActionResult<Product>> PostProductInStock(int id, int addToStock) {
            var product = await _context.Products.FindAsync(id);
            if (product == null) {
                return NotFound(new { message = $"Product with ID {id} not found." });
            }

            product.InStock +=addToStock;

            await _context.SaveChangesAsync();

            return Ok(new { message = $"Product {id} updated to inTtock by '{addToStock}'." });
        }
    }
}
