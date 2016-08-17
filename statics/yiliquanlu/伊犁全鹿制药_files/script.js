$(document).ready(function() {	
	var lastScrollTop = 0;
	$(window).scroll(function() {
		var wintop = $(window).scrollTop(), docheight = $(document).height(), winheight = $(window).height()/1.5;
		// Global Nav Show Hide
		if( wintop >= winheight && wintop < ((winheight*9) + (winheight/2)) )$('.section2_Xq').fadeIn(300),$('.section3_Xq').fadeIn(300),$('.section4_Xq').fadeIn(300),$('.section5_Xq').fadeIn(300),$('.section6_Xq').fadeIn(300),$('#cy11').fadeIn(500),$('#cy14').fadeIn(800),$('#cy15').fadeIn(1000), $('#cy17').fadeIn(1200)
		else $('.section2_Xq').fadeOut(1),$('.section3_Xq').fadeOut(1),$('.section4_Xq').fadeOut(1),$('.section5_Xq').fadeOut(1),$('.section6_Xq').fadeOut(1),$('#cy11').fadeOut(1),$('#cy14').fadeOut(1),$('#cy15').fadeOut(1),$('#cy17').fadeOut(1)
		
		
	});
});
