document.addEventListener('DOMContentLoaded', function() {
    // Get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Auto-update quantity in cart via AJAX
    function updateCartQuantity(productId, newQuantity) {
        const csrftoken = getCookie('csrftoken');

        fetch(`update/${productId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken
            },
            body: `qty=${newQuantity}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Cart updated successfully');
                // Optional: reload page to show updated totals
                // location.reload();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to update cart');
        });
    }

    // Quantity increment
    document.querySelectorAll('.bootstrap-touchspin-up').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.getAttribute('data-product-id');

            if (productId) {
                // Cart page - auto-save
                const input = document.getElementById('quantity_' + productId);
                if (input) {
                    let currentVal = parseInt(input.value) || 1;
                    input.value = currentVal + 1;
                    updateCartQuantity(productId, input.value);
                }
            } else {
                // Product page - just update input
                const input = this.closest('.quantity').querySelector('input[name="qty"]');
                if (input) {
                    let currentVal = parseInt(input.value) || 1;
                    input.value = currentVal + 1;
                }
            }
        });
    });

    // Quantity decrement
    document.querySelectorAll('.bootstrap-touchspin-down').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.getAttribute('data-product-id');

            if (productId) {
                // Cart page - auto-save
                const input = document.getElementById('quantity_' + productId);
                if (input) {
                    let currentVal = parseInt(input.value) || 1;
                    if (currentVal > 1) {
                        input.value = currentVal - 1;
                        updateCartQuantity(productId, input.value);
                    }
                }
            } else {
                // Product page - just update input
                const input = this.closest('.quantity').querySelector('input[name="qty"]');
                if (input) {
                    let currentVal = parseInt(input.value) || 1;
                    if (currentVal > 1) {
                        input.value = currentVal - 1;
                    }
                }
            }
        });
    });
});


