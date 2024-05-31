// Variables to write a review
const writeReviewLink = document.getElementById("write-review");
const reviewModal = new bootstrap.Modal(document.getElementById("reviewModal"));

//Variables for edit
const editCommentButtons = document.getElementsByClassName("edit-comment-button");
const reviewText = document.getElementById("id-body");
const reviewForm = document.getElementById("reviewForm");
const editConfirm = document.getElementById("editConfirm");

//Variables for delete 
const deleteCommentButtons = document.getElementsByClassName("delete-comment-button");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

// To write reviews
writeReviewLink.addEventListener('click', () => {
    reviewForm.setAttribute("action", "write_review/");
    reviewModal.show();
});

// To edit reviews
for (let button of editCommentButtons) {
    button.addEventListener('click', (e) => {
        let reviewId = e.target.getAttribute('data-review_id');
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        // reviewText.value = reviewContent;
        reviewForm.setAttribute("action", `edit_review/${reviewId}/`);
        reviewModal.show();
    });
}

// To delete comments
for (let button of deleteCommentButtons) {
    button.addEventListener('click', (e) => {
        let reviewId = e.target.getAttribute('data-review_id');
        deleteConfirm.setAttribute("href", `delete_review/${reviewId}`);
        deleteModal.show();
    });
}