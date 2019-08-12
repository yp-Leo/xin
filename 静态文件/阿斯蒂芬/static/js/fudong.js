$(function(){
	  
	   var fixedTop = 130;
	   $('div.fd').css({top:fixedTop+'px'}); 
	   
		$('div.ftt').click(function(){
			$('body,html').animate({scrollTop:0},500)
			})
	   $(window).scroll(scrolls)
	   scrolls()
	   function scrolls(){
		   
		 
		   var blackTop = $('div.ftt')
		   var sTop = $(window).scrollTop();
		   
		   var topPx = sTop+fixedTop
		    $('div.fd').stop().animate({top:topPx});
			
		   if(sTop < 150){
			   
			   blackTop.fadeOut(300).css('display','none')
			   }
		   else{
			    
			   blackTop.fadeIn(300).css('display','block')
			   } 
		
		
	     }
	   })