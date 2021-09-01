const arrows = document.querySelectorAll(".arrow")
for (let arrow of arrows){
    let rotation = false
    arrow.addEventListener("click", ()=>{
        if (rotation == false){
            arrow.style.transform = "rotate(90deg)";
            rotation = true;
        }
        else{
            arrow.style.transform = "rotate(0)";
            rotation = false;
        }
    })
};