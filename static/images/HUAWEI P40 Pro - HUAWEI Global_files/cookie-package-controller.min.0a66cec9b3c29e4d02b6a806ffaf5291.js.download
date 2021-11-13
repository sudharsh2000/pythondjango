function activeScriptNode(a){if(a.getAttribute("type")==="text/plain"){var b=a.cloneNode(true);
b.setAttribute("type","text/javascript");
a.parentNode.replaceChild(b,a)
}}function inactiveScriptNode(a){if(a.getAttribute("type")==="text/javascript"){var b=a.cloneNode(true);
b.setAttribute("type","text/plain");
a.parentNode.replaceChild(b,a)
}}function removeCookie(a){var b=new Date();
b.setDate(b.getDate()-1);
document.cookie=a+"="+escape("")+";expires="+b.toUTCString()+";"
}function activeCookieScripts(b){var a="."+b;
$(a).each(function(){activeScriptNode($(this)[0])
})
}$(function(){var a=getCookie("huawei_store_accept_cookie_flag");
if(a==="true"){if(!enableNewCookieCfg){activeCookieScripts("cookie-package-controller")
}else{if(ctlAnalysisCookie){activeCookieScripts("analysis-cookie")
}if(ctlAdvertiseCookie){activeCookieScripts("advertise-cookie")
}}}var b=$(".cookie-data").length>0?$(".cookie-data").attr("the-package-control-of-cookies-enabled"):"";
$(".convergent-cookie-agree").on("click",function(){if(!enableNewCookieCfg){activeCookieScripts("cookie-package-controller")
}else{if(ctlAnalysisCookie){activeCookieScripts("analysis-cookie")
}if(ctlAdvertiseCookie){activeCookieScripts("advertise-cookie")
}}});
$(".convergent-cookie-close").on("click",function(){if($(".convergent-cookie-agree").length>0){if(!enableNewCookieCfg&&b||enableNewCookieCfg&&(ctlAnalysisCookie||ctlAdvertiseCookie)){setJPCookie("huawei_store_accept_cookie_flag",true,360);
setJPCookie("huawei_store_accept_cookie_choose","1|0|0",360)
}else{setJPCookie("huawei_store_accept_cookie_flag",false,360);
setJPCookie("huawei_store_accept_cookie_choose","0|0|0",360)
}}})
});