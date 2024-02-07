/**
 * This script initializes a modal for deleting posts and sets up event listeners 
 * for both the modal and delete buttons associated with each post. 
 * It uses Bootstrap 5's modal component to show a confirmation dialog before deleting a post.
 */
document.addEventListener('DOMContentLoaded', () => {
    // Initialize the modal and the confirmation button within the modal
    const postModal = document.getElementById('postModal'); // The modal element
    const postDeleteConfirmButton = document.getElementById('postConfirm'); // The confirm button inside the modal

    // Create a Bootstrap 5 modal instance for 'postModal'
    const postDeleteModal = new bootstrap.Modal(postModal);

    /**
     * Add an event listener to the modal to set the delete URL when it's shown.
     * This captures the post's slug from the button that triggered the modal and 
     * updates the confirmation button's href attribute to include the correct delete URL.
     */
    postModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget; // The button that triggered the modal
        const postSlug = button.getAttribute('data-postslug'); // Extract the post slug from the button
        const postDeleteUrl = `/admin_dashboard/delete/${postSlug}/`; // Construct the delete URL using the post slug
        postDeleteConfirmButton.href = postDeleteUrl; // Update the confirmation button's href to the delete URL
    });

    // Select all buttons that trigger the modal
    const deletePostButtons = document.querySelectorAll('.delete-post-button');

    /**
     * Add an event listener to each delete button to show the modal when clicked.
     * This allows the user to confirm their intention to delete a post before proceeding.
     */
    deletePostButtons.forEach(button => {
        button.addEventListener("click", () => {
            postDeleteModal.show(); // Show the modal
        });
    });
});
