const arrows = document.querySelectorAll(".arrow");
const menus = document.querySelectorAll(".buttons-menu");

/* let components_list = []
for (let arrow of arrows){
    let components = [arrow]
    components_list.push(components)
}

for (let menu of menus){
    
} */

/* for (let arrow of arrows){
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
}; */

for (let ii in arrows){
    let arrow = arrows[ii];
    let menu = menus[ii];
    let rotation = false;
    arrow.addEventListener("click", ()=>{
        if (rotation == false){
            arrow.style.transform = "rotate(90deg)";
            menu.style.display = "block";
            rotation = true;
        }
        else{
            arrow.style.transform = "rotate(0)";
            menu.style.display = "none";
            rotation = false;
        }
    })
};