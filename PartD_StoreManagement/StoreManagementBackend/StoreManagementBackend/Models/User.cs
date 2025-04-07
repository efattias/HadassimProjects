using Microsoft.EntityFrameworkCore.Metadata.Internal;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text.Json.Serialization;

namespace StoreManagementBackend.Models
{
    public class User
    {
        [Key]
        public int Id { get; set; }

        [Required, MaxLength(20)]
        public string Username { get; set; }

        [Required, MaxLength(20)]
        public string Password { get; set; }

        [Required]
        [JsonConverter(typeof(JsonStringEnumConverter))]
        [Column(TypeName = "nvarchar(20)")]
        public Role Role { get; set; }

        [Required, MaxLength(50)]
        public string CompanyName { get; set; }

        [Required, MaxLength(20)]
        public string PhoneNumber { get; set; }

        [Required, MaxLength(20)]
        public string RepresentativeName { get; set; }

        [JsonIgnore]
        public ICollection<Product>? Products { get; set; }

        [JsonIgnore]
        public ICollection<Order>? Orders { get; set; }
    }
}
