// Load the modal content when the button is clicked
$("#open-form-modal").click(function() {
    $("#modal-container").load("../templates/forms/event_form.html", function() {
        // Show the modal after content is loaded
        $("#form-modal").show();
    });
});