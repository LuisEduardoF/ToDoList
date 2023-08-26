function change() {
    var x = document.getElementById("postit2").querySelector("#colors").value;
    colors = {"yellow": "#ffe28c", "green":"#d5e5a3", "brown":"#d6c1ab", "blue":"#b8d8d8", "purple":"#baa9ba", "orange":"#ff8f5e"}
    document.getElementById("postit2").style.backgroundColor = colors[x];

    var x = document.getElementById("postit").querySelector("#colors").value;
    colors = {"yellow": "#ffe28c", "green":"#d5e5a3", "brown":"#d6c1ab", "blue":"#b8d8d8", "purple":"#baa9ba", "orange":"#ff8f5e"}
    document.getElementById("postit").style.backgroundColor = colors[x]; 
      
}

function submit() {
    $.ajax({
        type: "POST",
        url: '/main/add',
        data: {
            name: $("#id_name").val(),
            date: $("#id_date").val(),
            description: $("#id_description").val(),
            color: $("#colors").val()
        },
        dataType: "json",
    });
};

function change_note() {
    $.ajax({
        type: "POST",
        url: '/main/change',
        data: {
            name: document.getElementById("postit2").querySelector("#id_name").value,
            date: document.getElementById("postit2").querySelector("#id_date").value,
            description: document.getElementById("postit2").querySelector("#id_description").value,
            color: document.getElementById("postit2").querySelector("#colors").value,
            id: document.getElementById("postit2").querySelector("span[name=id]").value,
        },
        dataType: "json",
    });
    location.reload();
};

function delete_note() {
    $.ajax({
        type: "POST",
        url: '/main/delete',
        data: {
            name: document.getElementById("postit2").querySelector("#id_name").value,
            date: document.getElementById("postit2").querySelector("#id_date").value,
            description: document.getElementById("postit2").querySelector("#id_description").value,
            color: document.getElementById("postit2").querySelector("#colors").value,
            id: document.getElementById("postit2").querySelector("span[name=id]").value,
        },
        dataType: "json",
    });
    location.reload();
};

$('#close').click(function() {
    $('#exampleModal').modal('hide');
});
$('#submit').click(function() {
    $('#exampleModal').modal('hide');
    location.reload();
});;
