document.addEventListener("DOMContentLoaded", function (){
    var inputs = document.querySelectorAll("input.subject-check")


    for (var input of inputs) {
        var parent = input.parentNode;
        var grandparent = parent.parentNode;
        grandparent.insertBefore(input, parent);
        grandparent.setAttribute("style", "margin-right: 15px;")

        input.classList.remove("subject-check");
        input.className += "btn-check";
        input.type = "checkbox";
        input.autocomplete = "off";

        parent.className += "btn btn-outline-primary"
        console.log(parent)
    
    }
    var grandGrandParent = grandparent.parentNode;
    grandGrandParent.setAttribute("style", "display: flex; flex-wrap: wrap;");

})