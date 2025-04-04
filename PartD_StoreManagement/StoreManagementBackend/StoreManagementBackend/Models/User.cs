using System.ComponentModel.DataAnnotations;

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
        public Role Role { get; set; }

        [Required, MaxLength(50)]
        public string CompanyName { get; set; }

        [Required, MaxLength(20)]
        public string PhoneNumber { get; set; }

        [Required, MaxLength(20)]
        public string RepresentativeName { get; set; }

        public ICollection<Product>? Products { get; set; }
        public ICollection<Order>? Orders { get; set; }
    }
}
