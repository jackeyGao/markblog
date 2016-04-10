// File Name: static/markbook/home.js
// Author: JackeyGao
// mail: gaojunqi@outlook.com
// Created Time: 五  4/ 8 15:09:49 2016

$(function() {
    var curtain = $('.curtain');
    curtain.toggle();
    curtain.slideDown(1000);
});

$(function() {
    // archives 
    $(".archives ul.hidearch").hide();
    $(".archives h4.downarch").click(function() {
        $(this).next().slideToggle('fast');
        return false;
    });
});
