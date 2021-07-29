function onImgClick(click){
    imageContainer = document.getElementById("modal-image")
    src = click.target.getAttribute("src")
    
    iVal = src.indexOf("?")
    newSrc = src.substring(0, iVal) + "?encoding=webp&x=1920"

    imageContainer.setAttribute("src", newSrc)

    $('#bigPicModal').on('hidden.bs.modal', function (e) {
        imageContainer = document.getElementById("modal-image")
        imageContainer.setAttribute("src", "")
        console.log("lol")
    })

    $('#bigPicModal').modal("toggle")
}

function addImgClickListeners(){
    images = document.getElementsByClassName('quater-img')
    for(i in images){
        try{
            images[i].addEventListener("click", onImgClick)
        }catch(error){
        }
    }
}

window.onload = addImgClickListeners