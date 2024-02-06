document.addEventListener('DOMContentLoaded', () => {
    const deleteModal = document.getElementById('deleteModal');
    deleteModal.addEventListener('show.bs.modal', function (event) {
        // Button that triggered the modal
        const button = event.relatedTarget;
        // Extract info from data-* attributes
        const postSlug = button.getAttribute('data-postslug');
        // Dynamically construct the delete URL based on the post's slug
        const deleteUrl = `/admin_dashboard/delete/${postSlug}/`;
        // Find the delete confirmation button in the modal and set its href to the delete URL
        const deleteConfirmButton = deleteModal.querySelector('#deleteConfirm');
        deleteConfirmButton.href = deleteUrl;
    });
});

