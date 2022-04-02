const SubmitForm = (form_name) => {
    var form = document.getElementsByName(form_name)[0];
    form.submit();
}

const imageClick = () => {
    SubmitForm("image_form")
}