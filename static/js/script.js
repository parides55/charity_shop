const removalModal = new bootstrap.Modal(document.getElementById("removalModal"));
const removeButtons = document.getElementsByClassName("btn-to-remove-item");
const removeConfirm = document.getElementById("removeConfirm");

console.log("starting now")

for (let button of removeButtons) {
    button.addEventListener('click', (e) => {
        console.log('click')
        let itemId = e.target.getAttribute('data-basket_id');
        console.log(itemId)
        removeConfirm.href = `remove_item/${itemId}`;
        removalModal.show();
    });
    
}