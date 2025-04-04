using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace StoreManagementBackend.Models
{
    public class Product
    {
        [Key]
        public int Id { get; set; }

        [Required, MaxLength(30)]
        public string ProductName { get; set; }

        [Required, Column(TypeName = "decimal(6,2)")]
        public decimal PricePerItem { get; set; }

        [Required]
        public int MinimumQuantity { get; set; }

        [Required]
        public int InStock { get; set; }

        [Required]
        public int SupplierId { get; set; }

        [ForeignKey("SupplierId")]
        public User Supplier { get; set; }

        public ICollection<OrderItem>? OrderItems { get; set; }
    }
}
