using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text.Json.Serialization;

namespace StoreManagementBackend.Models
{
    public class Order
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public int SupplierId { get; set; }

        [ForeignKey("SupplierId")]
        [JsonIgnore]
        public User? Supplier { get; set; }

        [Required]
        public DateTime InvitedDate { get; set; } = DateTime.Now;

        public DateTime? ApprovalDate { get; set; }

        public DateTime? CompleteDate { get; set; }

        [Required]
        [Column(TypeName = "nvarchar(15)")]
        [JsonConverter(typeof(JsonStringEnumConverter))]
        public Status Status { get; set; }

        [JsonIgnore]
        public ICollection<OrderItem>? OrderItems { get; set; }
    }
}
