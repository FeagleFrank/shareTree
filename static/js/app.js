var customContextMenu = function(e,id,parent_id,type){
//    console.log("id:"+n);
    e.preventDefault();
    e.stopPropagation();
    type=type||1;
    var menu=document.querySelector("#contextMenu");
    menu.style.left=e.clientX+'px';
    menu.style.top=e.clientY+'px';
    if(type===1){
        menu.innerHTML="<div class=\"add_node\">增加节点</div><div class=\"add_child_node\">增加子节点</div><div class=\"add_article\">增加文章</div><div class=\"del_node\">删除节点</div>";
        menu.style.height='100px';
    }else{
        menu.innerHTML="<div class=\"contextMenu add_node\">增加节点</div>";
        menu.style.height='25px';
    }
    // var pre_onclick=window.onclick;
    window.onclick=function(e){
        document.querySelector("#contextMenu").style.height=0;
        // window.onclick=pre_onclick;
    };
    console.log(parent_id);
    document.querySelector(".add_node").onclick = function(){
        var name = prompt("请输入节点名");
        if(name){
            add_node(parent_id,name);
        }
    };
    document.querySelector(".add_child_node").onclick = function(){
        var name = prompt("请输入节点名");
        if(name){
            add_node(id,name);
        }
    };
    document.querySelector(".del_node").onclick = function(){
        if(confirm("是否删除该节点?")){
            del_node(id);
        }
    };
    document.querySelector(".add_article").onclick = function(){
        var name = prompt("请输入文章名");
        var author = prompt("请输入作者名")
        if(name){
            add_article(id,name,author);
        }
    };

};

var add_node = function(parent_id,name){
    $.ajax({
        type:"post",
        url:"/addNode",
        data:{parent_id:parent_id,name:name},
        success:function(){
            window.location.reload();
        }
    })
};

var del_node = function(id){
    $.ajax({
        type:"post",
        url:"/delNode",
        data:{id:id},
        success:function(){
            window.location.reload();
        }
    })
};

var add_article = function(id,name,author){
    $.ajax({
        type:"post",
        url:"/addArticle",
        data:{id:id,name:name,author:author},
        success:function(){
            window.location.reload();
        }
    })
}

