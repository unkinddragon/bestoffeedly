// var $myjq;
// function getScript(){
//     var script=document.createElement('script');
//     script.src='jquery_my.js';
//     var head=document.getElementsByTagName('head')[0],
//     done=false;
//     // Attach handlers for all browsers
//     script.onload=script.onreadystatechange = function(){
//         if ( !done && (!this.readyState
//             || this.readyState == 'loaded'
//             || this.readyState == 'complete') ) {
//             done=true;
//             $myjq=jQuery.noConflict();
//             script.onload = script.onreadystatechange = null;
//         }
//     };
//     head.appendChild(script);
// }
/*
title is here:
<a href="http://www.cnews.ru/news/line/2016-06-27_bolee_2_mln_rossiyan_zaregistrirovalis_na_portale" id="tc/ww8EU3snQHOXN7MKc9qd83wTQVsk77s9vXdX0Ct0=_15591e68863:48fe4d4:85ca5f35_entry_title" class="entryTitle title read" target="_blank" cdf_container="10">Более&nbsp;2 млн россиян зарегистрировались на портале «Почты России»</a>

short summary:
<div class="content" itemprop="description" id="tc/ww8EU3snQHOXN7MKc9qd83wTQVsk77s9vXdX0Ct0=_15591e68863:48fe4d4:85ca5f35_entryContent" cdf_container="3"> 
На интернет-портале pochta.ru более 2 млн пользователей завели личные кабинеты, синхронизированные с мобильным п 
</div>

url is inside the positive link:

/*

Send positive example when clicking this link:
<a href="http://www.cnews.ru/news/line/2016-06-27_bolee_2_mln_rossiyan_zaregistrirovalis_na_portale" class="fx-button secondary full-width" style="margin-top:24px" target="_blank"> 
Visit Website 
</a>
*/

/*
Send negative example when clicking this link:
<img data-buryentryid="tc/ww8EU3snQHOXN7MKc9qd83wTQVsk77s9vXdX0Ct0=_15591e68863:48fe4d5:85ca5f35" src="images/condensed-close-black.png" title="Mark as read and hide">
*/

function positive() {
	//alert('That was good!');
	console.log('good');
	url = this.getAttribute('href');
	date = new Date().toLocaleString();
	console.log(url);
	$.get('http://localhost:5000/store/good?url=' + encodeURIComponent(url) + '&date=' + encodeURIComponent(date));
}
function negative() {
	//alert('That was bad!');
	console.log('bad');
	url = $(this).parent('.condensedTools').children('a').prop('href');
	date = new Date().toLocaleString();
	title = $(this).parent('.condensedTools').parent('div').children('div:last').children('div:last').children('a').text();
	summary = $(this).parent('.condensedTools').parent('div').children('div:last').children('div:last').children('span').text();
	
	console.log(url);
	$.get('http://localhost:5000/store/bad?url=' + encodeURIComponent(url) + '&date=' + encodeURIComponent(date) + '&title=' + encodeURIComponent(title) + '&summary=' + encodeURIComponent(summary));
}
function waitForFeedLoad() {
    if ($('.u0Entry').length == 0) {
        setTimeout(waitForFeedLoad,50);
    }
    else {
    	console.log('feed loaded.');
    	doStuff();
    }
}
function setPositive() {
	$(document).on('click', '.fx-button.full-width', positive);
	console.log('positive set.');
}
function setNegative() {
	$(document).on('click', '.condensedTools img', negative);
	// $('.condensedTools img').off('click', negative);
	// $('.condensedTools img').click( negative );
	console.log('negative set.');
	//setTimeout(setNegative, 500);
}
function setPositiveDelayed() {
	setTimeout(setPositive, 500);
}
function doStuff() {
	setPositive();
	//$('.title').click( setPositiveDelayed );
	setNegative();
	// $myjq('.fx-button.full-width').live('click', positive );
	// $myjq('.condensedTools img').live('click', negative );
	console.log('stuff done.');
}

waitForFeedLoad();