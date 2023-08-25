function change() {  
    var x = document.getElementById("colors").value;
    var modal = document.getElementById("postit");
    console.log(x, modal)
    colors = {"yellow": "#ffe28c", "green":"#d5e5a3", "brown":"#d6c1ab", "blue":"#b8d8d8", "purple":"#baa9ba", "orange":"#ff8f5e"}
    modal.style.backgroundColor = colors[x]
    console.log(colors)
}