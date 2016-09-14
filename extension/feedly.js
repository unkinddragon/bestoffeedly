var service_host = 'http://localhost:5000/store/'

function send_example(label, url, date, title, summary) {
	console.log(label + ': ' + url);
	request_url = service_host + '?';
	request_url += 'label=' + label;
	request_url += '&url=' + encodeURIComponent(url);
	request_url += '&date=' + encodeURIComponent(date);
	request_url += '&title=' + encodeURIComponent(title);
	request_url += '&summary=' + encodeURIComponent(summary);
	$.get(request_url);
}

function positive() {
	url = this.getAttribute('href');
	date = new Date().toLocaleString();
	title = '';
	summary = '';
	send_example('good', url, date, title, summary);
}
function negative() {
	url = $(this).parent('.condensedTools').children('a').prop('href');
	date = new Date().toLocaleString();
	title = $(this).parent('.condensedTools').parent('div').children('div:last').children('div:last').children('a').text();
	summary = $(this).parent('.condensedTools').parent('div').children('div:last').children('div:last').children('span').text();
	send_example('bad', url, date, title, summary);
}

function setPositive() {
	$(document).on('click', '.fx-button.full-width', positive);
	console.log('Positive trigger set.');
}

function setNegative() {
	$(document).on('click', '.condensedTools img', negative);
	console.log('Negative trigger set.');
}

function doStuff() {
	setPositive();
	setNegative();
	console.log('Triggers set.');
}

function waitForFeedLoad() {
    if ($('.u0Entry').length == 0) {
        setTimeout(waitForFeedLoad,50);
    }
    else {
    	console.log('Feed loaded.');
    	doStuff();
    }
}

waitForFeedLoad();