// erased

function myFunction() {
    a = document.getElementById('linkID').parentElement.parentElement.parentElement;
    $(a).slideToggle();

    if (document.getElementById("plusIcon").style.transform=="rotate(45deg)") {
        document.getElementById("plusIcon").style="transform: rotate(0deg)";
    }
    else {
        document.getElementById("plusIcon").style="transform: rotate(45deg)";
    }
}

