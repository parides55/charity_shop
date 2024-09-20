// Constants
const removalModal = new bootstrap.Modal(document.getElementById("removalModal"));
const removeButtons = document.getElementsByClassName("btn-to-remove-item");
const removeConfirm = document.getElementById("removeConfirm");

// Gets the item's id to be removed from the basket and initiates the removal modal
for (let button of removeButtons) {
    button.addEventListener('click', (e) => {
        let itemId = e.target.getAttribute('data-basket_id');
        removeConfirm.href = `remove_item/${itemId}`;
        removalModal.show();
    });
    
}

document.addEventListener('DOMContentLoaded', function() {
    // Get the PayPal container element
    const paypalButtonContainer = document.getElementById('paypal-button-container');
    
    // Retrieve the total amount and PayPal Client ID from the data attributes
    const totalAmount = paypalButtonContainer.getAttribute('data-total');
    const paypalClientId = paypalButtonContainer.getAttribute('data-paypal-client-id');
    
    // Load the PayPal SDK script dynamically
    const script = document.createElement('script');
    script.src = `https://www.sandbox.paypal.com/sdk/js?client-id=${paypalClientId}&currency=EUR`;
    script.onload = function() {
        // Initialize PayPal buttons once the script is loaded
        paypal.Buttons({
            style: {
                layout: 'vertical',
                color:  'gold',
                shape:  'rect',
                label:  'paypal',
                borderRadius: 10,
                height: 40,
            },
            createOrder: function(data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value: totalAmount // Pass the total amount from backend
                        }
                    }]
                });
            },
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(details) {
                    // Redirect the user after successful payment
                    window.location.href = '/after_payment';
                });
            },
            onCancel: function (data) {
                alert('Payment was cancelled!');
            },
            onError: function (err) {
                alert('An error occurred during the transaction.');
            }
        }).render('#paypal-button-container');
    };
    
    // Append the script to the document
    document.body.appendChild(script);
});