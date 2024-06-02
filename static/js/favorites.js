const favoriteRemovalModal = new bootstrap.Modal(document.getElementById("favoriteRemovalModal"));
const removeFavoriteButtons = document.getElementsByClassName('btn-to-remove-favorite');
const removeFavoriteConfirm = document.getElementById('removeFavoriteConfirm');

// Gets the favorite's id to be removed from the favorites and initiates the removal modal
for (let button of removeFavoriteButtons) {
    button.addEventListener('click', (e) => {
        let favoriteId = e.target.getAttribute('data-favorite_id');
        removeFavoriteConfirm.href = `remove_favorite/${favoriteId}`;
        favoriteRemovalModal.show();
    });
    
}