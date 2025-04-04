using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace StoreManagementBackend.Models
{
    public class Order
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public int SupplierId { get; set; }

        [ForeignKey("SupplierId")]
        public User Supplier { get; set; }

        [Required]
        public DateTime InvitedDate { get; set; } = DateTime.Now;

        public DateTime? ApprovalDate { get; set; }

        public DateTime? CompleteDate { get; set; }

        [Required]
        public Status Status { get; set; }

        public ICollection<OrderItem>? OrderItems { get; set; }
    }
}
