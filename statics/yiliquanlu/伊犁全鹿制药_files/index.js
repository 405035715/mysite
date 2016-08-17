/*

$(function(){
	$("#main .right .zhaopin ul .da:has(.tab)").each(function(index){
		$("#main .right .zhaopin .title2:eq("+index+")").toggle(function(){
		$("#main .right .zhaopin ul .da:eq("+index+")").children(".tab").stop(true,true).slideDown(500)
		$("#main .right .zhaopin .title2:eq("+index+")").addClass("hover")
		},function(){
		$("#main .right .zhaopin ul .da:eq("+index+")").children(".tab").stop(true,true).slideUp(500)
		$("#main .right .zhaopin .title2:eq("+index+")").removeClass("hover")
		})
	})
})
*/
$(function() {
    //集体调用
    $(".form input").each(function(){
        $(this).setDefauleValue();
    });
    //单个调用
    $("#key").setDefauleValue();
    $("#key2").setDefauleValue();
    $("#key3").setDefauleValue();
    $("#key4").setDefauleValue();
})
 
//设置input,textarea默认值
$.fn.setDefauleValue = function() {
    var defauleValue = $(this).val();
    $(this).val(defauleValue).css("color","#bcbcbc");
 
    return this.each(function() {       
        $(this).focus(function() {
            if ($(this).val() == defauleValue) {
                $(this).val("").css("color","#333");//输入值的颜色
            }
        }).blur(function() {
            if ($(this).val() == "") {
                $(this).val(defauleValue).css("color","#bcbcbc");//默认值的颜色
            }
        });
    });
}
/*

$(function(){
	$("#main .mains .mainCen .lie tr:odd").css("background","#f7f7f7")
})*/


$(function(){
	$("#header .search:has(.search1)").each(function(index){
		$("#header .search .sh:eq("+index+")").toggle(function(){
		$("#header .search:eq("+index+")").children(".search1").stop(true,true).slideDown(300)
		$("#header .search .sh:eq("+index+")").addClass("hover")
		},function(){
		$("#header .search:eq("+index+")").children(".search1").stop(true,true).slideUp(300)
		$("#header .search .sh:eq("+index+")").removeClass("hover")
		})
	})
})


$(function(){
	$(window).load(function()  {
	$("#fp-nav").height($(window).height());
	$(window).resize(function(){
	$("#fp-nav").height($(window).height());
	})

});
})

/*$(function(){
	var n1=document.documentElement.clientHeight
	$(".section1 .xia").click(function(){
		$("#dowebok-Wrap").animate({top:-n1},'slow')
		$("#fp-nav li a").removeClass("active")
		$("#fp-nav li a:eq(1)").addClass("active")
	})
})*/

$(function(){
	$(".section3_Xq .mainCase ul li a h3:even").css("padding-top","170px")
})

$(function(){
	$(".section2_Xq .chanye ul li dl dt a").each(function(index){
		$(".section2_Xq .chanye ul li dl dt a:eq("+index+")").hover(function(){
		$(".section2_Xq .chanye ul li dl dt a:eq("+index+")").stop().animate({'opacity':'1'},'slow')
		},function(){
		$(".section2_Xq .chanye ul li dl dt a:eq("+index+")").stop().animate({'opacity':'0'},'slow')
		})
	})
})


$(function() {
	var move=$('#banner');
		
	var window_w = $(window).width();
	
	if(window_w>1000){move.show();}

$('#tbNavLi1').click( function () {$('html,body').animate({scrollTop: $('#main').offset().top + 'px'},'slow');});
		
});

$(function(){
	$("#main .aboutMain .fengcais ul li:odd").addClass("last")
	$("#main .aboutMain .fengcais ul li:last").addClass("last2")
	$(".case ul li:odd").addClass("last")
	$("#main .joinMain ul li:last").addClass("last")
})
$(window).load(function() {
$(".erji").width($(window).width());
$(window).resize(function(){
$(".erji").width($(window).width());
})

});

$(window).load(function() {
$(".section ").height($(window).height());
$(window).resize(function(){
$(".section ").height($(window).height());
})

});

/*导航*/
$(function(){
 $(".nav ul li:has(div)").hover(function(){
  $(this).children("div").stop(true,true).slideDown(300)
  },function(){
  $(this).children("div").stop(true,true).slideUp(1)
  })
})


$(function (){
	$(".nav ul li").each(function(index){
		$(this).mouseover(function(){
			$(".nav ul li").removeClass("hover")//先删除所有的a的样式hover
			$(this).addClass("hover")//给对应的a添加样式hover
		})
		$(this).mouseout(function(){
			$(".nav ul li").removeClass("hover")//先删除所有的a的样式hover
		})
	})
})


$(function() {
	var move=$('#dowebok-Wrap');
		
	var window_w = $(window).width();
	
	if(window_w>1000){move.show();}

	$('.section1 .xia').click( function () {$('html,body').animate({scrollTop: $('.section2').offset().top + 'px'},'slow');});
		
});
$(function() {
	var move=$('#fp-nav');
		
	var window_w = $(window).width();
	
	if(window_w>1000){move.show();}

	$('.a1').click( function () {$('html,body').animate({scrollTop: $('.section1').offset().top + 'px'},'slow');});
	$('.a2').click( function () {$('html,body').animate({scrollTop: $('.section2').offset().top + 'px'},'slow');});
	$('.a3').click( function () {$('html,body').animate({scrollTop: $('.section3').offset().top + 'px'},'slow');});
	$('.a4').click( function () {$('html,body').animate({scrollTop: $('.section4').offset().top + 'px'},'slow');});
	$('.a5').click( function () {$('html,body').animate({scrollTop: $('.section5').offset().top + 'px'},'slow');});
	$('.a6').click( function () {$('html,body').animate({scrollTop: $('.section6').offset().top + 'px'},'slow');});
		
});


$(function(){
 $("#footer .last:has(strong)").hover(function(){
  $(this).children('strong').stop(true,true).slideDown(1)
  },function(){
  $(this).children('strong').stop(true,true).slideUp(1)
  })
})