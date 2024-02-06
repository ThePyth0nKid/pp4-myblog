document.addEventListener('DOMContentLoaded', () => {
    // Accessing the post deletion modal using the updated ID
    const deletePostModal = document.getElementById('deletePostModal');
    deletePostModal.addEventListener('show.bs.modal', function (event) {
        // Button that triggered the modal
        const button = event.relatedTarget;
        // Extract info from data-* attributes
        const postSlug = button.getAttribute('data-postslug');
        // Dynamically construct the delete URL based on the post's slug
        const deleteUrl = `/admin_dashboard/delete/${postSlug}/`;
        // Find the delete confirmation button in the modal using the updated ID and set its href to the delete URL
        const deletePostConfirmButton = deletePostModal.querySelector('#deletePostConfirm');
        deletePostConfirmButton.href = deleteUrl;
    });
});
