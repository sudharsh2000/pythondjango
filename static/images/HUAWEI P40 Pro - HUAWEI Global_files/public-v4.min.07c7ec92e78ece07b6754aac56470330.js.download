(function(a){if(typeof module==="object"&&module.exports){module.exports=a()
}else{var b=window.Granite=window.Granite||{};
b.Sling=a()
}}(function(){return{SELECTOR_INFINITY:".infinity",CHARSET:"_charset_",STATUS:":status",STATUS_BROWSER:"browser",OPERATION:":operation",OPERATION_DELETE:"delete",OPERATION_MOVE:"move",DELETE_SUFFIX:"@Delete",TYPEHINT_SUFFIX:"@TypeHint",COPY_SUFFIX:"@CopyFrom",MOVE_SUFFIX:"@MoveFrom",ORDER:":order",REPLACE:":replace",DESTINATION:":dest",SAVE_PARAM_PREFIX:":saveParamPrefix",IGNORE_PARAM:":ignore",REQUEST_LOGIN_PARAM:"sling:authRequestLogin",LOGIN_URL:"/system/sling/login.html",LOGOUT_URL:"/system/sling/logout.html"}
}));
(function(a){if(typeof module==="object"&&module.exports){module.exports=a()
}else{var b=window.Granite=window.Granite||{};
b.Util=a()
}}(function(){var a=function(b){return Object.prototype.toString.call(b)==="[object Array]"
};
return{patchText:function(d,c){if(c){if(!a(c)){d=d.replace("{0}",c)
}else{for(var b=0;
b<c.length;
b++){d=d.replace(("{"+b+"}"),c[b])
}}}return d
},getTopWindow:function(){var c=window;
if(this.iFrameTopWindow){return this.iFrameTopWindow
}try{while(c.parent&&c!==c.parent&&c.parent.location.href){c=c.parent
}}catch(b){}return c
},setIFrameMode:function(b){this.iFrameTopWindow=b||window
},applyDefaults:function(){var d;
var g=arguments[0]||{};
for(var c=1;
c<arguments.length;
c++){d=arguments[c];
for(var b in d){var f=d[b];
if(d.hasOwnProperty(b)&&f!==undefined){if(f!==null&&typeof f==="object"&&!(f instanceof Array)){g[b]=this.applyDefaults(g[b],f)
}else{if(f instanceof Array){g[b]=f.slice(0)
}else{g[b]=f
}}}}}return g
},getKeyCode:function(b){return b.keyCode?b.keyCode:b.which
}}
}));
(function(a){if(typeof module==="object"&&module.exports){module.exports=a(require("@granite/util"),require("jquery"))
}else{window.Granite.HTTP=a(Granite.Util,jQuery)
}}(function(util,$){return(function(){var contextPath=null;
var SCRIPT_URL_REGEXP=/^(?:http|https):\/\/[^/]+(\/.*)\/(?:etc\.clientlibs|etc(\/.*)*\/clientlibs|libs(\/.*)*\/clientlibs|apps(\/.*)*\/clientlibs|etc\/designs).*\.js(\?.*)?$/;
var ENCODE_PATH_REGEXP=/[^\w-.~%:/?[\]@!$&'()*+,;=]/;
var URI_REGEXP=/^(([^:/?#]+):)?(\/\/([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?/;
var loginRedirected=false;
var self={};
self.getSchemeAndAuthority=function(uri){if(!uri){return""
}var result=URI_REGEXP.exec(uri);
if(result===null){return""
}return[result[1],result[3]].join("")
};
self.getContextPath=function(){if(contextPath===null){contextPath=self.detectContextPath()
}return contextPath
};
self.detectContextPath=function(){try{if(window.CQURLInfo){contextPath=CQURLInfo.contextPath||""
}else{var scripts=document.getElementsByTagName("script");
for(var i=0;
i<scripts.length;
i++){var result=SCRIPT_URL_REGEXP.exec(scripts[i].src);
if(result){contextPath=result[1];
return contextPath
}}contextPath=""
}}catch(e){}return contextPath
};
self.externalize=function(url){try{if(url.indexOf("/")===0&&self.getContextPath()&&url.indexOf(self.getContextPath()+"/")!==0){url=self.getContextPath()+url
}}catch(e){}return url
};
self.internalize=function(url,doc){if(url.charAt(0)==="/"){if(contextPath===url){return""
}else{if(contextPath&&url.indexOf(contextPath+"/")===0){return url.substring(contextPath.length)
}else{return url
}}}if(!doc){doc=document
}var docHost=self.getSchemeAndAuthority(doc.location.href);
var urlHost=self.getSchemeAndAuthority(url);
if(docHost===urlHost){return url.substring(urlHost.length+(contextPath?contextPath.length:0))
}else{return url
}};
self.getPath=function(url){if(!url){if(window.CQURLInfo&&CQURLInfo.requestPath){return CQURLInfo.requestPath
}else{url=window.location.pathname
}}else{url=self.removeParameters(url);
url=self.removeAnchor(url)
}url=self.internalize(url);
var i=url.indexOf(".",url.lastIndexOf("/"));
if(i!==-1){url=url.substring(0,i)
}return url
};
self.removeAnchor=function(uri){var fragmentIndex=uri.indexOf("#");
if(fragmentIndex>=0){return uri.substring(0,fragmentIndex)
}else{return uri
}};
self.removeParameters=function(uri){var queryIndex=uri.indexOf("?");
if(queryIndex>=0){return uri.substring(0,queryIndex)
}else{return uri
}};
self.encodePathOfURI=function(uri){var DELIMS=["?","#"];
var parts=[uri];
var delim;
for(var i=0,ln=DELIMS.length;
i<ln;
i++){delim=DELIMS[i];
if(uri.indexOf(delim)>=0){parts=uri.split(delim);
break
}}if(ENCODE_PATH_REGEXP.test(parts[0])){parts[0]=self.encodePath(parts[0])
}return parts.join(delim)
};
self.encodePath=function(uri){uri=encodeURI(uri);
uri=uri.replace(/%5B/g,"[").replace(/%5D/g,"]");
uri=uri.replace(/\?/g,"%3F");
uri=uri.replace(/#/g,"%23");
return uri
};
self.handleLoginRedirect=function(){if(!loginRedirected){loginRedirected=true;
alert(Granite.I18n.get("Your request could not be completed because you have been signed out."));
var l=util.getTopWindow().document.location;
l.href=self.externalize("/")+"?resource="+encodeURIComponent(l.pathname+l.search+l.hash)
}};
self.getXhrHook=function(url,method,params){method=method||"GET";
if(window.G_XHR_HOOK&&typeof G_XHR_HOOK==="function"){var p={url:url,method:method};
if(params){p.params=params
}return G_XHR_HOOK(p)
}return null
};
self.eval=function(response){if(typeof response!=="object"){response=$.ajax({url:response,type:"get",async:false})
}try{return eval("("+(response.body?response.body:response.responseText)+")")
}catch(e){}return null
};
return self
}())
}));
(function(a){if(typeof module==="object"&&module.exports){module.exports=a(require("@granite/http"))
}else{window.Granite.I18n=a(window.Granite.HTTP)
}}(function(a){return(function(){var b={};
var h="/libs/cq/i18n/dict.";
var k=".json";
var c=undefined;
var j=false;
var g=null;
var l={};
var f=false;
var d=function(m){if(f){return h+m+k
}var o;
var n=document.querySelector("html");
if(n){o=n.getAttribute("data-i18n-dictionary-src")
}if(!o){return h+m+k
}return o.replace("{locale}",encodeURIComponent(m)).replace("{+locale}",m)
};
var i=function(o,n){if(n){if(Array.isArray(n)){for(var m=0;
m<n.length;
m++){o=o.replace("{"+m+"}",n[m])
}}else{o=o.replace("{0}",n)
}}return o
};
l.LOCALE_DEFAULT="en";
l.PSEUDO_LANGUAGE="zz";
l.PSEUDO_PATTERN_KEY="_pseudoPattern_";
l.init=function(m){m=m||{};
this.setLocale(m.locale);
this.setUrlPrefix(m.urlPrefix);
this.setUrlSuffix(m.urlSuffix)
};
l.setLocale=function(m){if(!m){return
}c=m
};
l.getLocale=function(){if(typeof c==="function"){c=c()
}return c||document.documentElement.lang||l.LOCALE_DEFAULT
};
l.setUrlPrefix=function(m){if(!m){return
}h=m;
f=true
};
l.setUrlSuffix=function(m){if(!m){return
}k=m;
f=true
};
l.getDictionary=function(m){m=m||l.getLocale();
if(!b[m]){j=m.indexOf(l.PSEUDO_LANGUAGE)===0;
try{var o=new XMLHttpRequest();
o.open("GET",a.externalize(d(m)),false);
o.send();
b[m]=JSON.parse(o.responseText)
}catch(n){}if(!b[m]){b[m]={}
}}return b[m]
};
l.get=function(q,n,o){var r;
var p;
var m;
r=l.getDictionary();
m=j?l.PSEUDO_PATTERN_KEY:o?q+" (("+o+"))":q;
if(r){p=r[m]
}if(!p){p=q
}if(j){p=p.replace("{string}",q).replace("{comment}",o?o:"")
}return i(p,n)
};
l.getVar=function(n,m){if(!n){return null
}return l.get(n,null,m)
};
l.getLanguages=function(){if(!g){try{var m=a.externalize("/libs/wcm/core/resources/languages.overlay.infinity.json");
var p=new XMLHttpRequest();
p.open("GET",m,false);
p.send();
var n=JSON.parse(p.responseText);
Object.keys(n).forEach(function(r){var q=n[r];
if(q.language){q.title=l.getVar(q.language)
}if(q.title&&q.country&&q.country!=="*"){q.title+=" ("+l.getVar(q.country)+")"
}});
g=n
}catch(o){g={}
}}return g
};
l.parseLocale=function(p){if(!p){return null
}var o=p.indexOf("_");
if(o<0){o=p.indexOf("-")
}var n;
var m;
if(o<0){n=p;
m=null
}else{n=p.substring(0,o);
m=p.substring(o+1)
}return{code:p,language:n,country:m}
};
return l
}())
}));
var hwPageType="support-v2";
$(function(){String.prototype.trimSpecial=function(b){if(b){return this.replace(new RegExp("^\\"+b+"+|\\"+b+"+$","g"),"")
}return this.replace(/^\s+|\s+$/g,"")
};
setTimeout(function(){$(".a-sup-common,#accountNumber,#accountHeader").on("click",function(){try{var d=$(this).attr("lab")?getContent($(this).attr("lab")):"Error: Not Maintain Value";
var c=$(this).attr("act")?getContent($(this).attr("act")):"Error: Not Maintain Value";
var b=$(this).attr("cat")?getContent($(this).attr("cat")):"Error: Not Maintain Value";
ga("send","event",b,c,d)
}catch(f){}})
},3000);
var a="expressRepaireServiceModify expressRepaireServiceSubmit repairStatusInquirySumbit doorToDoorServiceSubmit appointmentServiceModify appointmentServiceSubmit warrantyQuerySubmit topicPageInteractions topicListSiteSearch mailServiceSubmit homePageSiteSearch sparePartsPriceSubmit userCenterAdd userCenterModify userCenterDelete";
$(document).on(a,function(f){try{var b=DataLayerUtil.getEvent(f.type,"cat");
var c=DataLayerUtil.getEvent(f.type,"act");
var d=DataLayerUtil.getEvent(f.type,"lab");
ga("send","event",b,c,d)
}catch(g){}})
});
/*!
 * jQuery Cookie Plugin v1.4.1
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
(function(a){if(typeof define==="function"&&define.amd){define(["jquery"],a)
}else{if(typeof exports==="object"){a(require("jquery"))
}else{a(jQuery)
}}}(function(g){var a=/\+/g;
function d(j){return b.raw?j:encodeURIComponent(j)
}function h(j){return b.raw?j:decodeURIComponent(j)
}function i(j){return d(b.json?JSON.stringify(j):String(j))
}function c(j){if(j.indexOf('"')===0){j=j.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\")
}try{j=decodeURIComponent(j.replace(a," "));
return b.json?JSON.parse(j):j
}catch(k){}}function f(k,j){var l=b.raw?k:c(k);
return g.isFunction(j)?j(l):l
}var b=g.cookie=function(q,p,w){if(p!==undefined&&!g.isFunction(p)){w=g.extend({},b.defaults,w);
if(typeof w.expires==="number"){var r=w.expires,v=w.expires=new Date();
v.setTime(+v+r*86400000)
}return(document.cookie=[d(q),"=",i(p),w.expires?"; expires="+w.expires.toUTCString():"",w.path?"; path="+w.path:"",w.domain?"; domain="+w.domain:"",w.secure?"; secure":""].join(""))
}var x=q?undefined:{};
var u=document.cookie?document.cookie.split("; "):[];
for(var o=0,m=u.length;
o<m;
o++){var n=u[o].split("=");
var j=h(n.shift());
var k=n.join("=");
if(q&&q===j){x=f(k,p);
break
}if(!q&&(k=f(k))!==undefined){x[j]=k
}}return x
};
b.defaults={};
g.removeCookie=function(k,j){if(g.cookie(k)===undefined){return false
}g.cookie(k,"",g.extend({},j,{expires:-1}));
return !g.cookie(k)
}
}));
var LAG_SITE_CODE="zh_CN";
var LAG_SOURCE="100000007";
var LAG_CHANNEL_CODE="WEBSITE";
var LAG_COUNTRY_CODE=digitalData.page.pageInfo.countryCode;
var LAG_LANG="zh-cn";
var LAN_LANG_CODE="zh-cn";
var LAG_COUNTRY=digitalData.page.pageInfo.countryCode;
var LAG_LANGUAGE="zh-cn";
var LAG_APP_NUMBER="A182283838";
var LAG_MAP_ICO_URL="//consumer-res.huawei.com/etc/designs/huawei-cbg-site/clientlib-support-v2/asset/img/servicenet/map/{index}.png";
var __isAuth=($.cookie("__isAuth")==="true")?true:false;
var isCreateUserInfo=($.cookie("__isCreateUserInfo")==="true")?true:false;
var dcountryCode=digitalData.page.pageInfo.countryCode;
var regpostcode=/^[\s\S]*$/;
if(dcountryCode=="FR"){regpostcode=/^\d{5}$/
}else{if(dcountryCode=="UK"){regpostcode=/^[A-Za-z0-9][A-Za-z0-9 ]{3,6}[A-Za-z0-9]$/
}}var loginstate=-1;
var logininfo={};
var countryLangConfig={AE:{siteCode:"ar_AE",languageCode:"ar",casLangCode:"ar-ae",ccpdLangCode:"en"},BH:{siteCode:"en_BH",languageCode:"en",casLangCode:"en-bh",ccpdLangCode:"en"},EG:{siteCode:"ar_EG",languageCode:"ar",casLangCode:"ar-eg",ccpdLangCode:"en"},JO:{siteCode:"en_JO",languageCode:"en",casLangCode:"en-jo",ccpdLangCode:"en"},KW:{siteCode:"ar_KW",languageCode:"ar",casLangCode:"ar-kw",ccpdLangCode:"en"},LB:{siteCode:"en_LB",languageCode:"en",casLangCode:"en-lb",ccpdLangCode:"en"},SA:{siteCode:"ar_SA",languageCode:"ar",casLangCode:"ar-sa",ccpdLangCode:"en"},AZ:{siteCode:"az_AZ",languageCode:"az",casLangCode:"az-az"},BG:{siteCode:"bg_BG",languageCode:"bg",casLangCode:"bg-bg",ccpdLangCode:"en"},BA:{siteCode:"bs_BA",languageCode:"bs",casLangCode:"bs-ba",ccpdLangCode:"en"},CZ:{siteCode:"cs_CZ",languageCode:"cs",casLangCode:"cs-cz",ccpdLangCode:"en"},DK:{siteCode:"da_DK",languageCode:"da",casLangCode:"da-dk",ccpdLangCode:"en"},AT:{siteCode:"de_AT",languageCode:"de",casLangCode:"de-at",ccpdLangCode:"en"},CH:{siteCode:"de_CH",languageCode:"de",casLangCode:"de-ch"},DE:{siteCode:"de_DE",languageCode:"de",casLangCode:"de-de",ccpdLangCode:"en"},CY:{siteCode:"el_CY",languageCode:"el",casLangCode:"el-cy",ccpdLangCode:"en"},GR:{siteCode:"el_GR",languageCode:"el",casLangCode:"el-gr",ccpdLangCode:"en"},AU:{siteCode:"en_AU",languageCode:"en",casLangCode:"en-au",ccpdLangCode:"en"},BD:{siteCode:"en_BD",languageCode:"en",casLangCode:"en-us",ccpdLangCode:"en"},EN:{siteCode:"en_EN",languageCode:"en",casLangCode:"en-us"},ET:{siteCode:"en_ET",languageCode:"en",casLangCode:"en-us"},GB:{siteCode:"en_GB",languageCode:"en",casLangCode:"en-gb",ccpdLangCode:"en"},GH:{siteCode:"en_GH",languageCode:"en",casLangCode:"en-gh",ccpdLangCode:"en"},IE:{siteCode:"en_IE",languageCode:"en",casLangCode:"en-ie",ccpdLangCode:"en"},IN:{siteCode:"en_IN",languageCode:"en",casLangCode:"en-in",ccpdLangCode:"en"},IQ:{siteCode:"en_IQ",languageCode:"en",casLangCode:"en-us"},JM:{siteCode:"en_JM",languageCode:"en",casLangCode:"en-jm"},KE:{siteCode:"en_KE",languageCode:"en",casLangCode:"en-ke",ccpdLangCode:"en"},KH:{siteCode:"en_KH",languageCode:"en",casLangCode:"en-us",ccpdLangCode:"en"},LK:{siteCode:"en_LK",languageCode:"en",casLangCode:"en-us",ccpdLangCode:"en"},MU:{siteCode:"en_MU",languageCode:"en",casLangCode:"en-mu",ccpdLangCode:"en"},MY:{siteCode:"en_MY",languageCode:"en",casLangCode:"en-my",ccpdLangCode:"en"},NA:{siteCode:"en_NA",languageCode:"en",casLangCode:"en-na"},NG:{siteCode:"en_NG",languageCode:"en",casLangCode:"en-ng",ccpdLangCode:"en"},NP:{siteCode:"en_NP",languageCode:"en",casLangCode:"en-us"},NZ:{siteCode:"en_NZ",languageCode:"en",casLangCode:"en-nz",ccpdLangCode:"en"},OM:{siteCode:"en_OM",languageCode:"en",casLangCode:"en-us",ccpdLangCode:"en"},PH:{siteCode:"en_PH",languageCode:"en",casLangCode:"en-ph",ccpdLangCode:"en"},PK:{siteCode:"en_PK",languageCode:"en",casLangCode:"en-pk",ccpdLangCode:"en"},QA:{siteCode:"en_QA",languageCode:"en",casLangCode:"en-us",ccpdLangCode:"en"},SG:{siteCode:"en_SG",languageCode:"en",casLangCode:"en-sg",ccpdLangCode:"en"},TT:{siteCode:"en_TT",languageCode:"en",casLangCode:"en-tt"},TZ:{siteCode:"en_TZ",languageCode:"en",casLangCode:"en-tz"},UG:{siteCode:"en_UG",languageCode:"en",casLangCode:"en-ug"},US:{siteCode:"en_US",languageCode:"en",casLangCode:"en-us"},ZA:{siteCode:"en_ZA",languageCode:"en",casLangCode:"en-za",ccpdLangCode:"en"},ZM:{siteCode:"en_ZM",languageCode:"en",casLangCode:"en-zm"},AR:{siteCode:"es_AR",languageCode:"es",casLangCode:"es-ar",ccpdLangCode:"es"},BO:{siteCode:"es_BO",languageCode:"es",casLangCode:"es-bo",ccpdLangCode:"es"},CL:{siteCode:"es_CL",languageCode:"es",casLangCode:"es-cl",ccpdLangCode:"es"},CO:{siteCode:"es_CO",languageCode:"es",casLangCode:"es-co",ccpdLangCode:"es"},CR:{siteCode:"es_CR",languageCode:"es",casLangCode:"es-cr",ccpdLangCode:"es"},DO:{siteCode:"es_DO",languageCode:"es",casLangCode:"es-do",ccpdLangCode:"es"},EC:{siteCode:"es_EC",languageCode:"es",casLangCode:"es-ec",ccpdLangCode:"es"},ES:{siteCode:"es_ES",languageCode:"es",casLangCode:"es-es",ccpdLangCode:"es"},GT:{siteCode:"es_GT",languageCode:"es",casLangCode:"es-gt",ccpdLangCode:"es"},HN:{siteCode:"es_HN",languageCode:"es",casLangCode:"es-hn",ccpdLangCode:"es"},MX:{siteCode:"es_MX",languageCode:"es",casLangCode:"es-mx",ccpdLangCode:"es"},PA:{siteCode:"es_PA",languageCode:"es",casLangCode:"es-pa",ccpdLangCode:"es"},PE:{siteCode:"es_PE",languageCode:"es",casLangCode:"es-pe",ccpdLangCode:"es"},PY:{siteCode:"es_PY",languageCode:"es",casLangCode:"es-py",ccpdLangCode:"es"},SV:{siteCode:"es_SV",languageCode:"es",casLangCode:"es-sv",ccpdLangCode:"es"},UY:{siteCode:"es_UY",languageCode:"es",casLangCode:"es-uy",ccpdLangCode:"es"},VE:{siteCode:"es_VE",languageCode:"es",casLangCode:"es-ve"},EE:{siteCode:"et_EE",languageCode:"et",casLangCode:"et-ee",ccpdLangCode:"en"},IR:{siteCode:"fa_IR",languageCode:"fa",casLangCode:"fa-ir"},FI:{siteCode:"fi_FI",languageCode:"fi",casLangCode:"fi-fi",ccpdLangCode:"en"},CA:{siteCode:"fr_CA",languageCode:"fr",casLangCode:"fr-ca",ccpdLangCode:"en"},CD:{siteCode:"fr_CD",languageCode:"fr",casLangCode:"fr-cd"},CI:{siteCode:"fr_CI",languageCode:"fr",casLangCode:"fr-ci"},DZ:{siteCode:"fr_DZ",languageCode:"fr",casLangCode:"fr-dz",ccpdLangCode:"en"},FR:{siteCode:"fr_FR",languageCode:"fr",casLangCode:"fr-fr",ccpdLangCode:"en"},MA:{siteCode:"fr_MA",languageCode:"fr",casLangCode:"fr-ma",ccpdLangCode:"en"},TN:{siteCode:"fr_TN",languageCode:"fr",casLangCode:"fr-tn",ccpdLangCode:"en"},HR:{siteCode:"hr_HR",languageCode:"hr",casLangCode:"hr-hr",ccpdLangCode:"en"},HU:{siteCode:"hu_HU",languageCode:"hu",casLangCode:"hu-hu",ccpdLangCode:"en"},ID:{siteCode:"id_ID",languageCode:"id",casLangCode:"in-id",ccpdLangCode:"en"},IT:{siteCode:"it_IT",languageCode:"it",casLangCode:"it-it",ccpdLangCode:"en"},JP:{siteCode:"ja_JP",languageCode:"ja",casLangCode:"ja-jp",ccpdLangCode:"ja"},KR:{siteCode:"ko_KR",languageCode:"ko",casLangCode:"ko-kr",ccpdLangCode:"en"},LT:{siteCode:"lt_LT",languageCode:"lt",casLangCode:"lt-lt",ccpdLangCode:"en"},LV:{siteCode:"lv_LV",languageCode:"lv",casLangCode:"lv-lv",ccpdLangCode:"en"},MK:{siteCode:"mk_MK",languageCode:"mk",casLangCode:"mk-mk",ccpdLangCode:"en"},MM:{siteCode:"my_MM",languageCode:"my",casLangCode:"my-mm",ccpdLangCode:"en"},BE:{siteCode:"nl_BE",languageCode:"nl",casLangCode:"nl-be",ccpdLangCode:"en"},NL:{siteCode:"nl_NL",languageCode:"nl",casLangCode:"nl-nl",ccpdLangCode:"en"},NO:{siteCode:"no_NO",languageCode:"no",casLangCode:"nb-no",ccpdLangCode:"en"},PL:{siteCode:"pl_PL",languageCode:"pl",casLangCode:"pl-pl",ccpdLangCode:"en"},AO:{siteCode:"pt_AO",languageCode:"pt",casLangCode:"pt-ao"},PT:{siteCode:"pt_PT",languageCode:"pt",casLangCode:"pt-pt",ccpdLangCode:"en"},MD:{siteCode:"ro_MD",languageCode:"ro",casLangCode:"ro-md",ccpdLangCode:"en"},RO:{siteCode:"ro_RO",languageCode:"ro",casLangCode:"ro-ro",ccpdLangCode:"en"},RU:{siteCode:"ru_RU",languageCode:"ru",casLangCode:"ru-ru",ccpdLangCode:"ru"},SK:{siteCode:"sk_SK",languageCode:"sk",casLangCode:"sk-sk",ccpdLangCode:"en"},SI:{siteCode:"sl_SI",languageCode:"sl",casLangCode:"sl-si",ccpdLangCode:"en"},RS:{siteCode:"sr_RS",languageCode:"sr",casLangCode:"sr-sp",ccpdLangCode:"en"},SE:{siteCode:"sv_SE",languageCode:"sv",casLangCode:"sv-se",ccpdLangCode:"en"},TH:{siteCode:"th_TH",languageCode:"th",casLangCode:"th-th",ccpdLangCode:"en"},TR:{siteCode:"tr_TR",languageCode:"tr",casLangCode:"tr-tr",ccpdLangCode:"en"},UA:{siteCode:"uk_UA",languageCode:"uk",casLangCode:"uk-ua",ccpdLangCode:"en"},VN:{siteCode:"vi_VN",languageCode:"vi",casLangCode:"vi-vn",ccpdLangCode:"en"},CN:{siteCode:"zh_CN",languageCode:"zh-cn",casLangCode:"zh-cn"},CN1:{siteCode:"zh_CN",languageCode:"zh-cn",casLangCode:"zh-cn"},HK:{siteCode:"zh-tw_HK",languageCode:"zh-tw",casLangCode:"zh-hk"},TW:{siteCode:"zh-tw_TW",languageCode:"zh-tw",casLangCode:"zh-tw"},UK:{siteCode:"en_GB",languageCode:"en",casLangCode:"en-gb",ccpdLangCode:"en"},LEVANT:{siteCode:"en_LEVANT",languageCode:"en",casLangCode:"en-us"},FA:{siteCode:"fa_FA",languageCode:"fa",casLangCode:"fa-ir"},LATIN:{siteCode:"es_LATIN",languageCode:"es",casLangCode:"es-us",ccpdLangCode:"es"},IL:{siteCode:"he_IL",languageCode:"he",casLangCode:"he-il",ccpdLangCode:"en"},SD:{siteCode:"ar_SD",languageCode:"ar",casLangCode:"ar-sd"},BR:{siteCode:"pt_BR",languageCode:"pt",casLangCode:"pt-br",ccpdLangCode:"en"},KZ:{siteCode:"ru_KZ",languageCode:"ru",casLangCode:"ru-kz",ccpdLangCode:"en"},BY:{siteCode:"ru_BE",languageCode:"ru",casLangCode:"ru-by",ccpdLangCode:"en"},UZ:{siteCode:"ru_UZ",languageCode:"ru",casLangCode:"ru-ru",ccpdLangCode:"en"},LA:{siteCode:"lo_LA",languageCode:"lo",casLangCode:"lo-la",ccpdLangCode:"en"},CG:{siteCode:"fr_CG",languageCode:"fr",casLangCode:"fr-cg"},BW:{siteCode:"en_BW",languageCode:"en",casLangCode:"en-bw"}};
var sysConfig={siteCode:countryLangConfig[LAG_COUNTRY_CODE]?countryLangConfig[LAG_COUNTRY_CODE].siteCode:LAG_SITE_CODE,source:LAG_SOURCE,channelCode:LAG_CHANNEL_CODE,countryCode:LAG_COUNTRY_CODE,langCode:countryLangConfig[LAG_COUNTRY_CODE]?countryLangConfig[LAG_COUNTRY_CODE].languageCode:LAN_LANG_CODE,country:LAG_COUNTRY,language:countryLangConfig[LAG_COUNTRY_CODE]?countryLangConfig[LAG_COUNTRY_CODE].languageCode:LAN_LANG_CODE,mapIcoUrl:LAG_MAP_ICO_URL,lang:countryLangConfig[LAG_COUNTRY_CODE]?countryLangConfig[LAG_COUNTRY_CODE].languageCode:LAN_LANG_CODE,appNumber:LAG_APP_NUMBER,casLangCode:countryLangConfig[LAG_COUNTRY_CODE]?countryLangConfig[LAG_COUNTRY_CODE].casLangCode:LAN_LANG_CODE,ccpdLangCode:countryLangConfig[LAG_COUNTRY_CODE]?countryLangConfig[LAG_COUNTRY_CODE].ccpdLangCode:LAN_LANG_CODE};
sysConfig.reqClientType="27";
if(sysConfig.countryCode=="UK"){sysConfig.countryCode="GB";
sysConfig.country="GB"
}else{if(sysConfig.countryCode=="CN1"){sysConfig.countryCode="CN";
sysConfig.country="CN"
}else{if(sysConfig.countryCode=="EN"){sysConfig.countryCode="Global";
sysConfig.country="Global"
}else{if(digitalData.page.pageInfo.siteCode=="uses"){sysConfig.langCode="es";
sysConfig.language="es";
sysConfig.siteCode="en_US";
sysConfig.casLangCode="es-us";
sysConfig.countryCode="US"
}else{if(digitalData.page.pageInfo.siteCode=="saen"){sysConfig.langCode="en";
sysConfig.language="en";
sysConfig.siteCode="en_SA";
sysConfig.casLangCode="en-us";
sysConfig.countryCode="SA";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="sa"){sysConfig.langCode="ar";
sysConfig.language="ar";
sysConfig.siteCode="ar_SA";
sysConfig.casLangCode="ar-sa";
sysConfig.countryCode="SA"
}else{if(digitalData.page.pageInfo.siteCode=="aeen"){sysConfig.langCode="en";
sysConfig.language="en";
sysConfig.lang="en";
sysConfig.siteCode="en_AE";
sysConfig.casLangCode="en-us";
sysConfig.countryCode="AE";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="befr"){sysConfig.langCode="fr";
sysConfig.language="fr";
sysConfig.siteCode="fr_BE";
sysConfig.casLangCode="fr-be";
sysConfig.countryCode="BE";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="chfr"){sysConfig.langCode="fr";
sysConfig.language="fr";
sysConfig.siteCode="fr_CH";
sysConfig.casLangCode="fr-ch";
sysConfig.countryCode="CH"
}else{if(digitalData.page.pageInfo.siteCode=="kwen"){sysConfig.langCode="en";
sysConfig.language="en";
sysConfig.siteCode="en_KW";
sysConfig.casLangCode="en-us";
sysConfig.countryCode="KW";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="levantar"){sysConfig.langCode="ar";
sysConfig.language="ar";
sysConfig.siteCode="ar_LEVANT";
sysConfig.casLangCode="ar-eg";
sysConfig.countryCode="LEVANT";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="latinen"){sysConfig.langCode="en";
sysConfig.language="en";
sysConfig.siteCode="en_LATIN";
sysConfig.casLangCode="en-us";
sysConfig.countryCode="LATIN";
sysConfig.ccpdLangCode="es"
}else{if(digitalData.page.pageInfo.siteCode=="ca"){sysConfig.langCode="en";
sysConfig.language="en";
sysConfig.siteCode="en_CA";
sysConfig.casLangCode="en-ca";
sysConfig.countryCode="CA"
}else{if(digitalData.page.pageInfo.siteCode=="egen"){sysConfig.langCode="en";
sysConfig.language="en";
sysConfig.siteCode="en_EG";
sysConfig.casLangCode="en-us";
sysConfig.countryCode="EG"
}else{if(digitalData.page.pageInfo.siteCode=="mmen"){sysConfig.langCode="en";
sysConfig.language="en";
sysConfig.siteCode="en_MM";
sysConfig.casLangCode="en-us";
sysConfig.countryCode="MM";
sysConfig.ccpdLangCode="en"
}else{if(sysConfig.countryCode=="FA"){sysConfig.countryCode="AE";
sysConfig.country="AE";
sysConfig.siteCode="fa_AE";
sysConfig.ccpdLangCode="en"
}else{if(sysConfig.countryCode=="TW"){sysConfig.language="zh-cn"
}else{if(digitalData.page.pageInfo.siteCode=="lvru"){sysConfig.langCode="ru";
sysConfig.language="ru";
sysConfig.siteCode="ru_LV";
sysConfig.casLangCode="ru-lv";
sysConfig.countryCode="LV";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="eeru"){sysConfig.langCode="ru";
sysConfig.language="ru";
sysConfig.siteCode="ru_EE";
sysConfig.casLangCode="ru-ee";
sysConfig.countryCode="EE";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="mdru"){sysConfig.langCode="ru";
sysConfig.language="ru";
sysConfig.siteCode="ru_MD";
sysConfig.casLangCode="ru-md";
sysConfig.countryCode="MD"
}else{if(digitalData.page.pageInfo.siteCode=="qaar"){sysConfig.langCode="ar";
sysConfig.language="ar";
sysConfig.siteCode="ar_QA";
sysConfig.casLangCode="ar-qa";
sysConfig.countryCode="QA";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="omar"){sysConfig.langCode="ar";
sysConfig.language="ar";
sysConfig.siteCode="ar_OM";
sysConfig.casLangCode="ar-om";
sysConfig.countryCode="OM";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="bhar"){sysConfig.langCode="ar";
sysConfig.language="ar";
sysConfig.siteCode="ar_BH";
sysConfig.casLangCode="ar-bh";
sysConfig.countryCode="BH";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="joar"){sysConfig.langCode="ar";
sysConfig.language="ar";
sysConfig.siteCode="ar_JO";
sysConfig.casLangCode="ar-jo";
sysConfig.countryCode="JO";
sysConfig.ccpdLangCode="en"
}else{if(digitalData.page.pageInfo.siteCode=="lbar"){sysConfig.langCode="ar";
sysConfig.language="ar";
sysConfig.siteCode="ar_LB";
sysConfig.casLangCode="ar-lb";
sysConfig.countryCode="LB";
sysConfig.ccpdLangCode="en"
}}}}}}}}}}}}}}}}}}}}}}}}}var requestConfig={channelCode:sysConfig.channelCode,countryCode:sysConfig.countryCode,langCode:sysConfig.langCode,country:sysConfig.countryCode,language:sysConfig.language,siteCode:sysConfig.siteCode,ccpdLangCode:sysConfig.ccpdLangCode,groupCode:{}};
var casUrl="";
var apiurl="";
var cmktUrl="";
var cmscApiUrl="";
var huaweitimeApiUrl="";
if((typeof supportv2!="undefined")&&(typeof supportv2.apiBaseUrl!="undefined")){apiurl=supportv2.apiBaseUrl
}if((typeof supportv2!="undefined")&&(typeof supportv2.casUrl!="undefined")){casUrl=supportv2.casUrl
}var ccpcAuthUrl=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=huawei&loginUrl="+encodeURIComponent(casUrl+"/portal/login.html")+"&service="+encodeURIComponent(apiurl+"/web/weblogin/1000");
if((typeof supportv2!="undefined")&&(typeof supportv2.cmktApiUrl!="undefined")){cmktUrl=supportv2.cmktApiUrl
}if((typeof loginApiUrl!="undefined")&&(typeof loginApiUrl.cmscApiUrl!="undefined")){cmscApiUrl=loginApiUrl.cmscApiUrl
}if((typeof loginApiUrl!="undefined")&&(typeof loginApiUrl.huaweitimeApiUrl!="undefined")){huaweitimeApiUrl=loginApiUrl.huaweitimeApiUrl
}if(window.location.href.indexOf("debugClientLibs")<0){window.console.log=function(){}
}var apiSysConfig;
apiSysConfig={async:true,contentType:"application/x-www-form-urlencoded;charset=utf-8",enabledAjaxLoadingAnimate:false,ajaxAnimateGif:"img_con_v27_gif_loading.gif",authUrl:ccpcAuthUrl,outAuthUrl:apiurl+"/web/weblogout/1000",getAuthInfo:apiurl+"/web/getAuthorizationInfo/1000"};
var apiBase={request:function(h,b,l,j,f,k){if(apiurl==null||apiurl==""){return
}var d=b;
try{if(apiSysConfig.enabledAjaxLoadingAnimate==true){$("body").append('<div class="ajax-animate"></div>');
$(".ajax-animate").addClass("show")
}}catch(g){}var a=apiurl+h;
if(h.indexOf("http")==0){a=h
}var c;
if(f==null){c=apiSysConfig.async
}else{c=f
}var i="jsonp";
if(k!=null){i=k
}if(i=="jsonp"){if(sysConfig.countryCode=="MX"||sysConfig.countryCode=="CL"||sysConfig.countryCode=="PE"||sysConfig.countryCode=="CO"||sysConfig.countryCode=="LATIN"||sysConfig.countryCode=="AR"||sysConfig.countryCode=="BR"){$.ajax({url:a,type:"GET",dataType:"html",data:d,async:c,success:function(n){if(n.indexOf("(")>0){var m=n.split("(")[0];
n=n.replace(m,"");
n=n.substr(1,n.length)
}else{n=n.substr(1,n.length)
}n=n.substr(0,n.length-1);
n=JSON.parse(n);
try{if(n.responseCode!=null&&n.responseCode=="500002"){$.removeCookie("loginCallback",{path:"/"});
if(location.href.indexOf("/user-center")!=-1){if(!$(".user-center").data("isPreviewMode")){return
}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")));
return
}if(!isShowLogin()){return
}if(a.indexOf("/getServiceCust/1000")!=-1||a.indexOf("/getLeaguerInfo/1000")!=-1){if(location.href.indexOf("/express-repair/create")!=-1||location.href.indexOf("/reservation/create")!=-1||location.href.indexOf("/repair-appointment/create")!=-1||location.href.indexOf("/mail-feedback")!=-1){if($("#IS_PREVIEW_MODE").data("isPreviewMode")==false){return
}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")));
return
}}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=getLoginUri(null,false);
return
}}catch(o){}l&&l(n);
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
},complete:function(){},error:function(){j&&j();
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
}})
}else{$.ajax({url:a,type:"GET",dataType:"jsonp",jsonp:i,data:d,async:c,success:function(m){console.log(m);
try{if(m.responseCode!=null&&m.responseCode=="500002"){$.removeCookie("loginCallback",{path:"/"});
if(location.href.indexOf("/user-center")!=-1){if(!$(".user-center").data("isPreviewMode")){return
}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")));
return
}if(!isShowLogin()){return
}if(a.indexOf("/getServiceCust/1000")!=-1||a.indexOf("/getLeaguerInfo/1000")!=-1){if(location.href.indexOf("/express-repair/create")!=-1||location.href.indexOf("/reservation/create")!=-1||location.href.indexOf("/repair-appointment/create")!=-1||location.href.indexOf("/mail-feedback")!=-1){if($("#IS_PREVIEW_MODE").data("isPreviewMode")==false){return
}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")));
return
}}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=getLoginUri(null,false);
return
}}catch(n){}l&&l(m);
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
},complete:function(){},error:function(){j&&j();
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
}})
}}else{$.ajax({url:a,type:"GET",dataType:"jsonp",data:d,cache:true,async:c,jsonpCallback:i,success:function(m){console.log(m);
try{if(m.responseCode!=null&&m.responseCode=="500002"){$.removeCookie("loginCallback",{path:"/"});
if(location.href.indexOf("/user-center")!=-1){if(!$(".user-center").data("isPreviewMode")){return
}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")));
return
}if(!isShowLogin()){return
}if(a.indexOf("/getServiceCust/1000")!=-1||a.indexOf("/getLeaguerInfo/1000")!=-1){if(!$("#IS_PREVIEW_MODE").data("isPreviewMode")){return
}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}if(location.href.indexOf("/express-repair/create")!=-1||location.href.indexOf("/reservation/create")!=-1||location.href.indexOf("/repair-appointment/create")!=-1||a.indexOf("/getServiceCustV2/1000")!=-1||a.indexOf("/getLeaguerInfoV2/1000")!=-1){window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")));
return
}}removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=getLoginUri(null,false);
return
}}catch(n){}l&&l(m);
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
},complete:function(){},error:function(){j&&j();
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
}})
}},get:function(a,b){if(apiurl==null||apiurl==""){return
}$.ajax({url:apiurl+a,type:"GET",dataType:"json",async:apiSysConfig.async,success:function(c){console.log(c);
b&&b(c)
}})
},getJSONP:function(a,b){if(apiurl==null||apiurl==""){return
}$.ajax({url:apiurl+a,type:"GET",dataType:"jsonp",jsonp:"jsonp",async:apiSysConfig.async,success:function(c){console.log(c);
b&&b(c)
}})
},post:function(a,f,d,c){if(apiurl==null||apiurl==""){return
}var b="";
if(a.indexOf("http://")==0||a.indexOf("https://")==0){b=a
}else{b=apiurl+a
}$.ajax({url:b,type:"POST",dataType:"json",data:JSON.stringify(f),contentType:"application/json",async:apiSysConfig.async,xhrFields:{withCredentials:true},success:function(g){try{if(g.responseCode!=null&&g.responseCode=="500002"){if(location.href.indexOf("/user-center")!=-1){if(!$(".user-center").data("isPreviewMode")){return
}window.location.href=getLoginUri(null,false);
return
}if(!isShowLogin()){return
}if(b.indexOf("/getServiceCust/1000")!=-1||b.indexOf("/getLeaguerInfo/1000")!=-1||b.indexOf("/getServiceCustV2/1000")!=-1||b.indexOf("/getLeaguerInfoV2/1000")!=-1){var i=location.href;
if(i.indexOf("/express-repair/create")!=-1||i.indexOf("/reservation/create")!=-1||i.indexOf("/repair-appointment/create")!=-1||i.indexOf("/mail-feedback")!=-1||i.indexOf("/repair/pay")!=-1){if($("#IS_PREVIEW_MODE").data("isPreviewMode")==false){return
}window.location.href=getLoginUri(null,false);
return
}}window.location.href=getLoginUri(null,false);
return
}}catch(h){}d&&d(g)
},error:function(){c&&c()
}})
}};
var apiAuth={getAuthInfo:function(b,a){if(apiurl==null||apiurl==""){return
}if(isShowLogin()){if(a===true){$.ajax({url:apiSysConfig.getAuthInfo,type:"GET",dataType:"jsonp",jsonp:"jsonp",data:{},async:apiSysConfig.async,success:function(c){b&&b(c);
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
},complete:function(){},error:function(){$.ajax({url:apiSysConfig.getAuthInfo,type:"GET",dataType:"jsonp",jsonp:"jsonp",data:{},async:apiSysConfig.async,success:function(c){b&&b(c);
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
},complete:function(){},error:function(){error&&error();
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
}});
apiSysConfig.enabledAjaxLoadingAnimate&&$($(".ajax-animate")[0]).remove()
}})
}else{apiBase.request(apiSysConfig.getAuthInfo,{},b,function(){b(null)
})
}}},exitAuth:function(a){if(isShowLogin()||isUnifiedLoginSite()){apiBase.request(apiSysConfig.outAuthUrl,{},a,function(){a(null)
})
}}};
function getUrlParam(a){var b=new RegExp("(^|&)"+a+"=([^&]*)(&|$)");
var c=window.location.search.substr(1).match(b);
if(c!=null){return decodeURIComponent(c[2])
}return null
}function isLogin(){if(!!$.cookie("ac_loNa")){return true
}else{return false
}}function getLoginUri(a,c){if(casUrl==null||casUrl==""){return""
}var f=window.location.href;
var b;
var d;
if(f.indexOf("loginCallback=true")==-1){if(f.indexOf("?")>0){f=f+"&loginCallback=true"
}else{f=f+"?loginCallback=true"
}}if(a&&a!=""){if(a.indexOf("http://")==0||a.indexOf("https://")==0){f=a
}else{f=location.origin+a
}}var g=cmktUrl+"/login/cloudplatforms?siteURL="+encodeURIComponent(f);
if(c){f=f.replace("&loginCallback=true","").replace("?loginCallback=true","");
g=loginApiHost+"v1/login/casLogin?callback="+encodeURIComponent(f)+"&siteCode="+window.digitalData.page.pageInfo.siteCode2
}if($(window).width()>767){b=casUrl+"/portal/loginAuth.html";
d=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=red&loginUrl="+encodeURIComponent(b);
d+="&service="+encodeURIComponent(g)
}else{b=casUrl+"/mobile/standard/wapLogin.html";
d=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000002&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=huawei&loginUrl="+encodeURIComponent(b);
d+="&service="+encodeURIComponent(g)
}return d
}function getCmscLoginUri(a,d){if(casUrl==null||casUrl==""){return""
}var g=window.location.href;
var c;
var f;
var b=false;
if(d===true||d===false){b=d
}else{b=(isECommerceSite=="Self-eCommerce"||isECommerceSite=="Fusion-eCommerce")
}if(g.indexOf("loginCmscCallback=true")==-1){if(g.indexOf("?")>0){g=g+"&loginCmscCallback=true"
}else{g=g+"?loginCmscCallback=true"
}}if(a&&a!=""){if(a.indexOf("http://")==0||a.indexOf("https://")==0){g=a
}else{g=location.origin+a
}}var h=cmscApiUrl+"/login/cloudplatforms?siteURL="+encodeURIComponent(g);
if(b){g=g.replace("&loginCmscCallback=true","").replace("?loginCmscCallback=true","");
h=loginApiHost+"v1/login/casLogin?callback="+encodeURIComponent(g)+"&siteCode="+window.digitalData.page.pageInfo.siteCode2
}if($(window).width()>767){c=casUrl+"/portal/loginAuth.html";
f=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=red&loginUrl="+encodeURIComponent(c);
f+="&service="+encodeURIComponent(h)
}else{c=casUrl+"/mobile/standard/wapLogin.html";
f=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000002&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=huawei&loginUrl="+encodeURIComponent(c);
f+="&service="+encodeURIComponent(h)
}return f
}function getHuaweiTimeLoginUri(a,d){if(casUrl==null||casUrl==""){return""
}var g=window.location.href;
var c;
var f;
var b=false;
if(d===true||d===false){b=d
}else{b=(isECommerceSite=="Self-eCommerce"||isECommerceSite=="Fusion-eCommerce")
}if(g.indexOf("loginCallback=true")==-1){if(g.indexOf("?")>0){g=g+"&loginCallback=true"
}else{g=g+"?loginCallback=true"
}}if(a&&a!=""){if(a.indexOf("http://")==0||a.indexOf("https://")==0){g=a
}else{g=location.origin+a
}}var h=huaweitimeApiUrl+"/login/cloudplatforms?siteURL="+encodeURIComponent(g);
if(b){g=g.replace("&loginCallback=true","").replace("?loginCallback=true","");
h=loginApiHost+"v1/login/casLogin?callback="+encodeURIComponent(g)+"&siteCode="+window.digitalData.page.pageInfo.siteCode2
}if($(window).width()>767){c=casUrl+"/portal/loginAuth.html";
f=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=red&loginUrl="+encodeURIComponent(c);
f+="&service="+encodeURIComponent(h)
}else{c=casUrl+"/mobile/standard/wapLogin.html";
f=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000002&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=huawei&loginUrl="+encodeURIComponent(c);
f+="&service="+encodeURIComponent(h)
}return f
}function getAsyncUumLoginUri(b){var c=b||getNewUserUrl();
if(casUrl==null||casUrl==""||typeof(mktConfig)==="undefined"||mktConfig.uumApi==null||mktConfig.uumApi==""){return""
}var f=mktConfig.uumApi+"/v1/login/casLogin?callback="+encodeURIComponent(c)+"&siteCode="+window.digitalData.page.pageInfo.siteCode2.toUpperCase();
if(b){f+=($(window).width()<1199.98?"&clientType=95":"&clientType=85")
}else{f+=($(window).width()<1199.98?"&clientType=96":"&clientType=82")
}var a=casUrl+"/portal/loginAuth.html";
var d=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=red&loginUrl="+encodeURIComponent(a);
d+="&service="+encodeURIComponent(f);
return d
}function asyncUumLogin(a){if(window.sessionStorage&&window.sessionStorage.getItem("uumLoginStatus")==="1"){return
}if(casUrl!=null&&casUrl!=""&&typeof(mktConfig)!=="undefined"&&mktConfig.uumApi!=null&&mktConfig.uumApi!=""){$.ajax({type:"get",dataType:"jsonp",jsonp:"jsonp",url:getAsyncUumLoginUri(a),complete:function(){if(window.sessionStorage){window.sessionStorage.setItem("uumLoginStatus","1")
}}})
}}function asyncUumLogout(){if(casUrl!=null&&casUrl!=""&&typeof(mktConfig)!=="undefined"&&mktConfig.uumApi!=null&&mktConfig.uumApi!=""){$.ajax({type:"get",dataType:"jsonp",jsonp:"jsonp",url:mktConfig.uumApi+"/v1/logout/casLogout",complete:function(){}})
}}function getNewUserUrl(){var b="";
var a=supportv2.cmktApiUrl;
if(typeof(a)!="undefined"&&a!=""){b=a+"/services/service/extuser/info"
}return b
}function getRegisterUrl(b){var a="";
if(casUrl&&cmktUrl){if($(window).width()>1023){a=casUrl+"/portal/userRegister/"+(b=="phone"?"regbyphone.html":"regbyemail.html")+"?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&loginUrl="+encodeURIComponent(casUrl+"/portal/loginAuth.html")+"&service="+encodeURIComponent(cmktUrl+"/login/cloudplatforms?siteURL="+encodeURIComponent(location.href))+"&lang="+sysConfig.casLangCode+"&themeName=red"
}else{a=casUrl+"/mobile/standard/register/wapRegister.html?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&loginUrl="+encodeURIComponent(casUrl+"/mobile/standard/wapLogin.html")+"&service="+encodeURIComponent(cmktUrl+"/login/cloudplatforms?siteURL="+encodeURIComponent(location.href))+"&lang="+sysConfig.casLangCode+"&themeName=huawei"
}}return a
}function getWebsiteLogoutUrl(a){return casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent((a==null)?window.location.href:a))
}function getHuaweiAccount(){if(!$.cookie("_ext_u_e_")){return
}var a=getNewUserUrl();
if(a==null||a==""){return
}$.ajax({url:a,type:"GET",dataType:"jsonp",jsonp:"jsonp",success:function(b){if(b.resCode=="0"){try{window.encUser=b.cbg_uid
}catch(c){}if(b.crossSite&&b.crossSite=="1"){loginstate=1
}else{loginstate=0
}logininfo={cbgid:b.uid,name:b.userAccount,ac_loNa:b.ac_loNa,username:b.user};
if(getUrlParam("loginCallback")=="true"&&sysConfig.countryCode=="RU"){try{thirdPartyLogin()
}catch(c){}}}else{removeLoginCookie();
loginstate=3;
loginWhenExpires()
}},error:function(){loginstate=3
}})
}function getHuaweiAccountByRetry(){if(!$.cookie("_ext_u_e_")){return
}var a=getNewUserUrl();
if(a==null||a==""){return
}$.ajax({url:a,type:"GET",dataType:"jsonp",jsonp:"jsonp",success:function(b){if(b.resCode=="0"){try{window.encUser=b.cbg_uid
}catch(c){}if(b.crossSite&&b.crossSite=="1"){loginstate=1
}else{loginstate=0
}logininfo={cbgid:b.uid,name:b.userAccount,ac_loNa:b.ac_loNa,username:b.user};
if(getUrlParam("loginCallback")=="true"&&sysConfig.countryCode=="RU"){try{thirdPartyLogin()
}catch(c){}}}else{removeLoginCookie();
loginstate=3
}},error:function(){loginstate=3
}})
}function cmktLogin(){if(casUrl!=null&&casUrl!=""){$.ajax({type:"get",dataType:"jsonp",jsonp:"jsonp",url:getLoginUri(getNewUserUrl(),false),complete:function(){}})
}}function cmscLogin(){if(casUrl!=null&&casUrl!=""){$.ajax({type:"get",dataType:"jsonp",jsonp:"jsonp",url:getCmscLoginUri(getCmscNewUserUrl(),false),complete:function(){}})
}}function huaweiTimeLogin(){if(casUrl!=null&&casUrl!=""){$.ajax({type:"get",dataType:"jsonp",jsonp:"jsonp",url:getHuaweiTimeLoginUri(getNewUserUrl(),false),complete:function(){}})
}}function getCmscNewUserUrl(){var b="";
var a=loginApiUrl.cmscApiUrl;
if(typeof(a)!="undefined"&&a!=""){b=a+"/services/service/extuser/info"
}return b
}function processCmscAndHuaweiTimeLoginStatus(){if(typeof loginApiUrl==="undefined"){return
}var b=supportv2.cmktApiUrl;
var a=loginApiUrl.cmscApiUrl;
var c=loginApiUrl.huaweitimeApiUrl;
if(!!$.cookie("_ext_u_e_")){if(a!=null&&a!=""){$.ajax({url:a+"/services/service/extuser/info",type:"get",dataType:"jsonp",jsonp:"jsonp",success:function(d){if(d.resCode!="0"){cmscLogin()
}}})
}if(!$.cookie("userID")){if(c!=null&&c!=""){huaweiTimeLogin()
}}}else{if(!!$.cookie("userID")){if(b!=null&&b!=""){cmktLogin()
}if(a!=null&&a!=""){cmscLogin()
}}}}function processLoginStatus(){if(!!$.cookie("_ext_u_e_")){if($.cookie("loginCallback")!=="true"){isCompleteUserInfo()
}if(!isUnifiedLoginSite()){return
}var a="cbgcommunityUserinfo"+digitalData.page.pageInfo.countryCode;
if(location.href.indexOf("community")!==-1&&location.href.indexOf("community/login")===-1&&typeof getCookie==="function"&&!$.cookie(a)&&!$.cookie("forumLogin")){$.cookie("forumLogin","1",{path:"/"});
try{CommunityUserLogin.login()
}catch(c){}}if(!$.cookie("ec-loginStatus")){ecomLogin()
}}else{if((isECommerceSite==="Self-eCommerce"||isECommerceSite==="Fusion-eCommerce")&&typeof ecCom!="undefined"){var b=ecCom.isVisitor();
if((!b&&$.cookie("ec-loginStatus"))||$.cookie("cbgcommunityUserinfo"+digitalData.page.pageInfo.countryCode)){if(casUrl!=null&&casUrl!=""){$.ajax({type:"get",dataType:"jsonp",url:getLoginUri(getNewUserUrl(),false),complete:function(){isCompleteUserInfo(null,null,false);
loginstate=-1;
getHuaweiAccountByRetry()
}})
}}if(!b&&$.cookie("ec-loginStatus")){if(location.href.indexOf("community")!=-1&&!$.cookie("cbgcommunityUserinfo"+digitalData.page.pageInfo.countryCode)&&!$.cookie("forumLogin")){$.cookie("forumLogin","1",{path:"/"});
try{CommunityUserLogin.login()
}catch(c){}}}if(!$.cookie("ec-loginStatus")&&$.cookie("cbgcommunityUserinfo"+digitalData.page.pageInfo.countryCode)){ecomLogin()
}}}}function ecomLogin(){var a;
try{a=getLoginUri((loginApiHost+"v1/login/info?siteCode="+window.digitalData.page.pageInfo.countryCode),true);
if(a!=null&&a!=undefined&&a!=""&&(isUnifiedLoginSite())){$.ajax({url:a,type:"post",dataType:"jsonp",complete:function(c){window.sessionStorage.setItem("ec-loginStatus","1");
$.cookie("ec-loginStatus","1",{path:"/"})
}})
}}catch(b){}}function loginWhenExpires(){if(!isUnifiedLoginSite()){if(typeof cmktLogin==="function"){cmktLogin()
}}else{var a=!!((typeof ecCom!="undefined")&&ecCom.isVisitor());
if((!a&&$.cookie("ec-loginStatus"))||$.cookie("cbgcommunityUserinfo"+digitalData.page.pageInfo.countryCode)||$.cookie("_ext_u_e_")){$.ajax({type:"get",dataType:"jsonp",url:getLoginUri(getNewUserUrl(),false),complete:function(){isCompleteUserInfo(null,null,false);
loginstate=-1;
getHuaweiAccountByRetry()
}})
}else{if(location.href.indexOf("community")==-1){$(function(){apiAuth.exitAuth()
})
}}}}function isUnifiedLoginSite(){try{if(isECommerceSite){return isECommerceSite==="Self-eCommerce"||isECommerceSite==="Fusion-eCommerce"
}}catch(a){}return false
}function processPrivacy(){if($.cookie("agree-privacy-policy")=="1"){return
}if((sysConfig.countryCode=="GB"||isUnifiedLoginSite())&&location.href.indexOf("/community/")==-1){var b=500;
var a=setInterval(function(){if(loginstate==1||loginstate==0){var f=$(".cbg-support-privacy").val();
var c=$(".agree-privacy").val();
var d=$(".disagree-privacy").val();
showPrivacyPolicy({content:f,okStr:c,cancelStr:d,iconClass:"icon-warin"},function(){$.cookie("agree-privacy-policy","1",{path:"/"})
},function(){apiAuth.exitAuth(function(){removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")))
});
return
});
clearInterval(a)
}if(loginstate==3){clearInterval(a)
}if(b--<1){clearInterval(a)
}},20)
}}function processUumLoginStatus(){try{if(window.location.href.indexOf("loginCallback=true")!==-1&&$.cookie("_ext_u_e_")){asyncUumLogin()
}else{if(window.location.href.indexOf("loginCmscCallback=true")!==-1&&$.cookie("_cuef_u_e_")){asyncUumLogin(getCmscNewUserUrl())
}else{return
}}}catch(a){}}$(function(){if(($(".login-menu-component").length==0&&$(".huawei-v4 .login-v4-wrap .login-v4 .login-v4-cnt .show-login").length==0)){return
}getHuaweiAccount();
processUumLoginStatus();
if(sysConfig.siteCode=="en_EN"){return
}processCmscAndHuaweiTimeLoginStatus();
processLoginStatus();
var a=$(".login-menu-component").attr("data-support-login");
if(typeof(a)!="undefined"&&a=="no"){return
}$(".conv3_nav .icon_close").after($(".login-menu-component").html());
setTimeout(function(){$(".conv3_nav .navcon  .login-menu .login-btn").on("click",function(c){c.stopPropagation();
$("body").append("<style>@media screen and (max-width:767px){body.ready-login{ height:"+$(window).height()+"px; } body.ready-login .conv3_wrap,body.ready-login .foot_module{display:none!important;} }</style>");
menuPageHistory.ClosePage(function(){callLoginOnClick()
})
});
$(".conv3_nav .navcon  .login-menu").on("mouseenter",function(c){c.stopPropagation();
$(this).addClass("active")
});
$(".conv3_nav .navcon  .login-menu").on("click",function(c){c.stopPropagation();
if($(this).hasClass("active")){$(this).removeClass("active")
}else{$(this).addClass("active")
}});
$(".conv3_nav .navcon .login-menu").on("mouseleave",function(c){c.stopPropagation();
$(this).removeClass("active")
});
$(".conv3_nav .navcon .login-menu .my-exit,.conv3_wrap .user-center .my-exit,.user-info-header .user-info .my-exit").on("click",function(c){c.stopPropagation();
apiAuth.exitAuth(function(){removeLoginCookie();
window.location.href=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")))
})
});
if(isLogin()==false){$(".conv3_nav .navcon  .login-menu.singin").on("click",function(c){c.stopPropagation();
$.removeCookie("AuthorizationInfo",{path:"/"});
if(isLogin()){try{}catch(d){}window.location.href=$(".login-menu-component").attr("data-support-usercenter-url")
}else{}})
}else{$(".conv3_nav .navcon  .login-menu").addClass("singin");
var b=$.cookie("userHeadPicture");
if(b!=null&&b!=""){$("body").append("<style>.login-menu.singin,.login-menu.login-phone.singin .user-logined:before{  background-image:url("+b+") } .login-menu.singin .login-menu-contaner:after { content: '"+$.cookie("user")+"'; } </style>")
}$("body").append("<style>.login-menu.singin .login-menu-contaner:after { content: '"+$.cookie("user")+"'; }</style>");
setTimeout(function(){$(".login-menu.singin").click(function(c){c.stopPropagation();
if(isLogin()){try{}catch(d){}window.location.href=$(".login-menu-component").attr("data-support-usercenter-url")
}else{}if($(this).hasClass("active")){$(this).removeClass("active")
}else{$(this).addClass("active")
}})
})
}},200);
$(".huawei-v3 .header-wrap .right-box .login .login-wrap .login-cnt ul li.track-order-v3,.huawei-v3 .header-wrap .right-box .login .login-wrap .login-cnt ul li.app-track-order-v3").on("click",function(b){b.stopPropagation()
})
});
function webLogout(){removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}__isAuth=false;
isCreateUserInfo=false;
if(isECommerceSite=="Self-eCommerce"||isUnifiedLoginSite()){if(casUrl!=null&&casUrl!=""){$.ajax({type:"get",dataType:"jsonp",url:casUrl+"/logout?service="+supportv2.cmktApiUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent(getNewUserUrl()),success:function(){}});
apiAuth.exitAuth()
}}else{apiAuth.exitAuth()
}}function getSitUrl(a){var c=a?a:"";
var b=window.location.origin+"/"+siteCode+"/"+c;
return b
}function huaweitimeLogout(a){if(loginApiUrl.huaweitimeApiUrl!=null&&loginApiUrl.huaweitimeApiUrl!=""){$.ajax({type:"get",dataType:"jsonp",url:casUrl+"/logout?service="+encodeURIComponent(loginApiUrl.huaweitimeApiUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent(getNewUserUrl())),complete:function(){a&&a()
}})
}}function cmscLogout(a){if(casUrl!=null&&casUrl!=""&&loginApiUrl.cmscApiUrl!=null&&loginApiUrl.cmscApiUrl!=""){$.ajax({type:"get",dataType:"jsonp",url:casUrl+"/logout?service="+encodeURIComponent(loginApiUrl.cmscApiUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent(getCmscNewUserUrl())),complete:function(){a&&a()
}})
}}function callLogin(a){if(!isShowLogin()){return
}webLogout();
callLoginOnClick(a)
}function callLoginOnClick(a){if(!isShowLogin()){return
}if(casUrl==null||casUrl==""){return
}$(".login-dialog-component .login-dialog").css("display","block");
$("body").addClass("ready-login");
$("body").append("<style>@media screen and (max-width:767px){ body.ready-login{height:"+($(window).height()-0)+"px; } }</style>");
setTimeout(function(){$(".login-dialog").addClass("show")
},0);
setTimeout(function(){var d=window.location.href;
if(d.indexOf("loginCallback=true")==-1){if(d.indexOf("?")>0){d=d+"&loginCallback=true"
}else{d=d+"?loginCallback=true"
}}if(a&&a!=""){if(a.indexOf("http://")==0||a.indexOf("https://")==0){d=a
}else{d=location.origin+a
}}var f=cmktUrl+"/login/cloudplatforms?siteURL="+encodeURIComponent(d);
var b;
var c;
if($(window).width()>767){b=casUrl+"/portal/loginAuth.html";
c=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000000&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=red&loginUrl="+encodeURIComponent(b);
c+="&service="+encodeURIComponent(f)
}else{b=casUrl+"/mobile/standard/wapLogin.html";
c=casUrl+"/remoteLogin?reqClientType="+sysConfig.reqClientType+"&loginChannel=27000002&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&themeName=huawei&loginUrl="+encodeURIComponent(b);
c+="&service="+encodeURIComponent(f)
}$("#loginFrame").attr("src",c);
$(".login-close").on("click",function(){$(".login-dialog").removeClass("show");
setTimeout(function(){$(".login-dialog").css("display","none");
$("body").removeClass("ready-login")
},300)
})
},200)
}function needLogin(a){if(!isShowLogin()){return
}if(typeof a=="undefined"){a=$(".user-center").data("isPreviewMode")
}if(!!$.cookie("ac_loNa")){setTimeout(function(){if(a==false){return
}isCompleteUserInfo(function(b,c){if(c=="500002"){return
}})
},2000)
}else{$(function(){setTimeout(function(){if(a==false){return
}window.location.href=getLoginUri(null,false)
},200)
});
apiAuth.exitAuth(function(){removeLoginCookie();
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}})
}}function isShowLogin(){if(isECommerceSite=="Self-eCommerce"||isECommerceSite=="Fusion-eCommerce"){return true
}var a=$(".login-menu-component").attr("data-support-login")||$(".huawei-v4 .login-v4-wrap .login-v4 .login-v4-cnt .show-login").attr("data-support-login");
if(typeof(a)!="undefined"&&a=="no"){return false
}return true
}$(function(){setTimeout(function(){$("[data-auth-href]").each(function(){$(this).on("click",function(c){var b=this;
var a=$(this).attr("data-auth-href");
if(isShowLogin()){$.ajax({url:apiurl+"/web/getAuthorizationInfo/1000",type:"GET",dataType:"jsonp",jsonp:"jsonp",data:{},async:true,success:function(d){if(d.responseCode=="200"){window.location.href=$(b).attr("data-auth-href")
}else{$.removeCookie("loginCallback",{path:"/"});
if(location.href.indexOf("/express-repair")!=-1||location.href.indexOf("/reservation")!=-1||location.href.indexOf("/repair-appointment")!=-1){window.location.href=getLoginUri(a,false)
}else{window.location.href=getLoginUri(location.href,false)
}}}})
}else{window.location.href=$(b).attr("data-auth-href")
}})
})
},1000)
});
function authCallback(a){window.location.reload();
if(a.responseCode=="200"){window.location.reload()
}else{}}function removeLoginCookie(){$.removeCookie("ac_loNa",{path:"/"});
$.removeCookie("user",{path:"/"});
$.removeCookie("userHeadPicture",{path:"/"});
$.removeCookie("AuthorizationInfo",{path:"/"});
$.removeCookie("__isAuth",{path:"/"});
$.removeCookie("__isCreateUserInfo",{path:"/"});
$.removeCookie("loginCallback",{path:"/"});
if(window.sessionStorage){window.sessionStorage.removeItem("uumLoginStatus")
}}function removeUnifiedLoginCookie(){try{var a="cbgcommunityUserinfo"+digitalData.page.pageInfo.countryCode;
$.removeCookie(a,{path:"/"});
$.removeCookie("cbgLoginTag",{path:"/"});
sessionStorage.getItem("ec-loginStatus")?sessionStorage.removeItem("ec-loginStatus"):"";
$.removeCookie("ec-loginStatus",{path:"/"});
$.removeCookie("login_status",{path:"/"});
$.removeCookie("forumLogin",{path:"/"});
$.removeCookie("user",{path:"/"+window.digitalData.page.pageInfo.siteCode2+"/"});
$.removeCookie("ac_loNa",{path:"/"+window.digitalData.page.pageInfo.siteCode2+"/"});
$.removeCookie("loginUserinfo",{path:"/"+window.digitalData.page.pageInfo.siteCode2+"/"})
}catch(b){}}function isCompleteUserInfo(d,b,c){if(!isShowLogin()){return
}if(apiurl==null||apiurl==""){return
}var a={};
a.accountId="000";
a.source=sysConfig.source;
$(function(){if($.cookie("loginCallback")==="true"){apiAuth.getAuthInfo(function(f){if(f!=null&&f.responseCode=="500002"){removeLoginCookie();
if(c!=false){window.location.href=getLoginUri(null,false)
}}else{if(f.responseCode=="200"){if(__isAuth){d&&d(isCreateUserInfo,f.responseCode);
return false
}}}},true)
}else{if(__isAuth){d&&d(isCreateUserInfo);
return false
}if(casUrl==null||casUrl==""){return
}$.ajax({type:"get",url:apiSysConfig.authUrl,dataType:"jsonp",jsonp:"jsonp",complete:function(){$.cookie("loginCallback","true",{path:"/"});
thirdPartyLogin()
}})
}})
}function showPrivacyPolicy(b,d,a){var c="<div class='s-dialog-fr-privacy'>   <div class='s-content-dialog'>       <div class='s-dialog-title'>       </div><div class='s-dialog-content'>"+b.content+"       </div><div class='s-dialog-btn'>           <a class='s-btn s-cancel-btn'>"+b.cancelStr+"</a>           <a class='s-btn s-ok-btn'>"+b.okStr+"</a>       </div>   </div></div>";
$("body").append(c);
setTimeout(function(){$(".s-dialog-fr-privacy .s-content-dialog").toggleClass("s-show")
},0);
$(".s-dialog-fr-privacy .s-ok-btn").on("click",function(){$(".s-dialog-fr-privacy .s-content-dialog").toggleClass("s-show");
$(this).off("click");
setTimeout(function(){$("body > .s-dialog-fr-privacy").remove();
d&&d()
},500);
$(".s-dialog-fr-privacy .s-ok-btn,.s-dialog-fr-privacy .s-cancel-bt").off("click")
});
$(".s-dialog-fr-privacy  .s-cancel-btn").on("click",function(){$(".s-dialog .s-content-dialog").toggleClass("s-show");
$(this).off("click");
setTimeout(function(){$("body > .s-dialog-fr-privacy").remove();
a&&a()
},500);
$(".s-dialog-fr-privacy .s-ok-btn,.s-dialog-fr-privacy .s-cancel-bt").off("click")
})
}function thirdPartyLogin(){var a=$("i.third-party-login-url");
if(a){var b=$("i.third-party-login-url").attr("data-callback-url");
if(b){$.ajax({type:"get",url:b,dataType:"jsonp",jsonp:"jsonp",complete:function(){}})
}}else{return
}}var apiIRetail={getHotline:function(a,c){var b=a;
b.countryCode=requestConfig.countryCode;
b.langCode=requestConfig.langCode;
apiBase.request("/iRetail/getHotline/1000",b,c)
}};
function checkStorageStatus(){var b=false;
try{if(window.localStorage){b=true
}}catch(a){}return b
}function buildNewKownApplicableRegion(a){if(sysConfig.countryCode=="Global"){a.applicable_region="0"
}else{if(digitalData.page.pageInfo.siteCode=="latin"){a.applicable_region="CO"
}else{if(digitalData.page.pageInfo.siteCode=="latinen"){a.applicable_region="US"
}else{if(digitalData.page.pageInfo.siteCode=="levantar"){a.applicable_region="EG"
}else{if(digitalData.page.pageInfo.siteCode=="levant"){a.applicable_region="US"
}else{a.applicable_region=sysConfig.countryCode
}}}}}return a
}function checkInputStr(b){var a=/^[^"#&'\+;<=>\\]{0,1000}$/;
return a.test(b)
}function getLoginStates(b){var a=$.cookie("_ext_u_e_");
if(a&&(a=="1"||a==1)){b&&b()
}else{apiAuth.exitAuth(function(){removeLoginCookie();
if($(".huawei-v4 .login-v4-wrap .login-v4 .login-v4-cnt .show-login").length>0){var c=getWebsiteLogoutUrl($(".huawei-v4 .login-v4-wrap .login-v4 .login-v4-cnt .show-login").attr("data-support-url"))
}else{var c=casUrl+"/logout?service="+encodeURIComponent(cmktUrl+"/logout/cloudplatforms?siteURL="+encodeURIComponent($(".login-menu-component").attr("data-support-url")))
}window.location.href=c
})
}}var login_leave="";
$(function(){if($(window).width()>1023){if($("#header-v3 .nav-wrap .login").length==0){return
}}else{if($(".app-nav .app-nav-wrap .app-login-icon").length==0){return
}}$(".login-cnt .login-other-items").on("click",function(b){b.stopPropagation()
});
setTimeout(function(){$("#header-v3 .nav-wrap .login .signInBtn, .app-nav .app-login-icon .signInBtn").on("click",function(a){if(typeof(communityLogin)!="undefined"){return
}a.stopPropagation();
window.location.href=getLoginUri()
});
$("#header-v3 .nav-wrap .login").on("mouseenter",function(a){a.stopPropagation();
$(this).addClass("active");
clearTimeout(login_leave)
});
$("#header-v3 .nav-wrap .login, .app-nav .app-login-icon").on("click",function(a){a.stopPropagation();
if($(this).hasClass("active")){$(this).removeClass("active")
}else{$(this).addClass("active")
}});
$("#header-v3 .nav-wrap .login").on("mouseleave",function(a){a.stopPropagation();
var b=$(this);
login_leave=setTimeout(function(){b.removeClass("active")
},300)
});
$(".app-login-bullet .app-sign .app-loginout").on("click",function(a){if(typeof(communityLogin)!="undefined"){return
}window.location.href=$(".app-login-bullet .app-sign .app-loginout").attr("data-url")
});
$("#header-v3 .nav-wrap .login .my-exit,.conv3_wrap .user-center .my-exit,.user-info-header .user-info .my-exit, .app-nav .app-login-icon .my-exit").on("click",function(a){a.stopPropagation();
apiAuth.exitAuth(function(){$.removeCookie("ac_loNa",{path:"/"});
$.removeCookie("user",{path:"/"});
$.removeCookie("userHeadPicture",{path:"/"});
$.removeCookie("AuthorizationInfo",{path:"/"});
$.removeCookie("__isAuth",{path:"/"});
$.removeCookie("__isCreateUserInfo",{path:"/"});
$.removeCookie("loginCallback",{path:"/"});
$.removeCookie("agree-privacy-policy",{path:"/"});
if(isUnifiedLoginSite()){removeUnifiedLoginCookie()
}var b=encodeURIComponent($(".login-menu-component").attr("data-support-url"));
if(location.href.indexOf("/community/")!=-1&&(isUnifiedLoginSite())){b=encodeURIComponent(location.href);
if(location.href.indexOf("/community/user-center")!=-1||location.href.indexOf("/login/")!=-1){b=encodeURIComponent(location.href.substring(0,location.href.lastIndexOf("/community/"))+"/community/")
}}window.location.href=casUrl+"/logout?service="+encodeURIComponent($(".login-menu-component").attr("data-support-cmkt-url")+"/logout/cloudplatforms?siteURL="+b)
})
});
if(isLogin()==false){$("#header-v3 .nav-wrap .login.singin, .app-nav .app-login-icon.singin").on("click",function(a){a.stopPropagation();
$.removeCookie("AuthorizationInfo");
if(isLogin()){try{}catch(b){}window.location.href=$(".login-menu-component").attr("data-support-usercenter-url")
}else{}})
}else{$("#header-v3 .nav-wrap .login, .app-nav .app-login-icon").addClass("singin");
$(".login-cnt .shop-bag-bnt").on("click",function(a){a.stopPropagation()
});
$(".login.singin .show-logout .singin-user,.app-login-icon.singin  .app-sign-user .singin-user").text($.cookie("user"));
setTimeout(function(){$(".login.singin").click(function(a){a.stopPropagation();
if(isLogin()){try{}catch(b){}window.location.href=$(".login-menu-component").attr("data-support-usercenter-url")
}else{}if($(this).hasClass("active")){$(this).removeClass("active")
}else{$(this).addClass("active")
}})
})
}},200)
});
function forumLogin(b){var a=window.location.href;
var c="https://"+clientLoginUrl+loginPort+"/oauth2/v2/authorize?reqClientType="+reqClientType+"&response_type=code&client_id="+clientID+"&redirect_uri=https%3A%2F%2F"+window.location.host+"%2F"+digitalData.page.pageInfo.siteCode2+"%2Fcommunity%2Flogin%2F&scope=https%3A%2F%2Fwww.huawei.com%2Fauth%2Faccount%2Fbase.profile&display=page&lang="+sysConfig.casLangCode;
b&&(c=b);
setCookieCommunity("currentUrl",getCookieUri(),24);
if(window.location.href.indexOf("/community")==-1){setCookieCommunity("cbgcommunitylogin","1",24)
}window.location.href=c
}function forumMobileLogin(){window.location.href="https://"+clientUrl+"/CAS/mobile/standard/register/wapRegister.html?reqClientType="+reqClientType+"&loginChannel="+loginChannel+"&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&loginUrl=https%3A%2F%2F"+clientUrl+"%2FCAS%2Fportal%2Flogin.html&service=https%3A%2F%2F"+clientLoginUrl+"%2Foauth2%2Fv2%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3D"+clientID+"%26redirect_uri%3Dhttps%253A%252F%252F"+window.location.host+"%252F"+digitalData.page.pageInfo.siteCode2+"%252Fcommunity%252Flogin%252F%26scope%3Dhttps%253A%252F%252Fwww.huawei.com%252Fauth%252Faccount%252Fbase.profile%26display%3Dpage"
}function forumLogout(){var b=$("#forum-clientLogoutUrl").val();
var a=window.location.href;
if(a.indexOf("/community")==-1){setCookieCommunity("cbgcommunitylogout","1",24)
}window.location.href=b
}function forumMobileLogout(){var d=ajaxUrl+"user/logout";
var c;
if(getCookieCommunity("tk")){c=getCookieCommunity("tk")
}var f={};
if(SITE_CODE=="worldwide"){f.site=digitalData.page.pageInfo.siteCode
}else{f.site=SITE_CODE
}if(getCookieCommunity("loginUserinfo")){var b=JSON.parse(getCookieCommunity("loginUserinfo"));
f.loginUserId=b.userId
}else{return
}var a=window.location.protocol+"//"+window.location.host+"/"+digitalData.page.pageInfo.siteCode2;
f.redirectUri=encodeURIComponent(a);
$.ajax({url:d,type:"post",data:JSON.stringify(f),dataType:"json",xhrFields:{withCredentials:true},headers:{CSRFToken:c},crossDomain:true,contentType:"application/json",success:function(i,g,h){$(".forum-login,.app-login-icon").removeClass("singin");
delCookieCommunity("currentUrl");
delCookieCommunity("cbgcommunitylogin");
if(h.getResponseHeader("CSRFToken")){c=h.getResponseHeader("CSRFToken");
delCookieCommunity("tk");
setCookieCommunity("tk",h.getResponseHeader("CSRFToken"),24)
}if(i.resultCode=="1"||!i.resultCode){if(getCookieCommunity("loginUserinfo")){delCookieCommunity("loginUserinfo")
}if(getCookieCommunity("blacklist")){delCookieCommunity("blacklist",false)
}if(window.localStorage&&window.localStorage.getItem("pactList")){window.localStorage.removeItem("pactList")
}if(i&&i.url){window.location.href=i.url
}else{window.location.href="/"+digitalData.page.pageInfo.siteCode2
}}else{CommunityLoginFailTipDialog(i.resultMsg,function(){})
}},error:function(j,g,h){if(j.getResponseHeader("CSRFToken")){c=j.getResponseHeader("CSRFToken");
setCookieCommunity("tk",j.getResponseHeader("CSRFToken"),24)
}if(j&&j.responseJSON){CommunityLoginFailTipDialog(j.responseJSON.resultMsg,function(){})
}else{var i=$("#forum-networkplroblemtips").val();
CommunityLoginFailTipDialog(i,function(){})
}}})
}function setCookieCommunity(b,c,a){var d=new Date();
d.setTime(d.getTime()+a*60*60*1000);
document.cookie=b+"="+escape(c)+((a==null)?"":";expires="+d.toGMTString())+";path=/"+digitalData.page.pageInfo.siteCode2+"/;"
}function getCookieCommunity(b){if(document.cookie.length>0){var c=document.cookie.indexOf(b+"=");
if(c!=-1){c=c+b.length+1;
var a=document.cookie.indexOf(";",c);
if(a==-1){a=document.cookie.length
}return unescape(document.cookie.substring(c,a))
}}return""
}function delCookieCommunity(a){var b=new Date();
b.setTime(b.getTime()-1);
var c=getCookieCommunity(a);
if(c!=null&&c!=""){document.cookie=a+"=;expires="+b.toGMTString()+";path=/"+digitalData.page.pageInfo.siteCode2+"/;"
}}function getLoginStateCommunity(){var a=getCookieCommunity("loginUserinfo");
if(a&&a!=""){$(".forum-login,.app-login-icon").addClass("singin")
}else{$(".forum-login,.app-login-icon").removeClass("singin")
}}function getCookieUri(){var a=window.location.pathname;
a=a.substring(1,a.length);
a=a.substring(a.indexOf("/")+1,a.length);
if(a==""){a=" "
}return a
}function popWindowInHomepageCommunity(){var a=getCookieCommunity("popcommunity");
if(a&&a!=""){return
}else{setTimeout(function(){$(".forum-home-mask").show()
},500);
setCookieCommunity("popcommunity","1",720)
}}function goAccountCenter(){var a=window.location.href;
var c=a.substring(0,a.lastIndexOf("user-center"));
var b="https://"+clientUrl+"/AMW/portal/userCenter/index.html?loginChannel=40005000&reqClientType=3040&lang="+sysConfig.casLangCode+"&service="+c+"/login/";
window.open(b)
}function CommunityLoginFailTipDialog(b,c){var a="<div class='community-dialog'>   <div class='s-info-dialog'>       <div class='s-info-title'>           <h3><span class='fail-icon'></span>"+b+"</h3>       </div>   </div></div>";
$("body").append(a);
setTimeout(function(){$(".community-dialog .s-info-dialog").toggleClass("s-show");
setTimeout(function(){$(".community-dialog .s-info-dialog").css("opacity",0);
setTimeout(function(){$("body > .community-dialog").remove();
c&&c()
},1600)
},1600)
},0)
}$(function(){if(typeof(communityLogin)=="undefined"){return
}getLoginStateCommunity();
if(digitalData.page.category.pageType=="homepage"&&$("#forum-showPop").val()=="1"){popWindowInHomepageCommunity()
}$(".forum-login .signInBtn, .app-nav .forum-login-app .signInBtn").click(function(){forumLogin()
});
$(".forum-login .registeredBtn").click(function(){var a="https://"+clientUrl+"/CAS/portal/userRegister/regbyphone.html?reqClientType="+reqClientType+"&loginChannel="+loginChannel+"&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&loginUrl=https%3A%2F%2F"+clientUrl+"%2FCAS%2Fportal%2Flogin.html&service=https%3A%2F%2F"+clientLoginUrl+"%2Foauth2%2Fv2%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3D"+clientID+"%26redirect_uri%3Dhttps%253A%252F%252F"+window.location.host+"%252F"+digitalData.page.pageInfo.siteCode2+"%252Fcommunity%252Flogin%252F%26scope%3Dhttps%253A%252F%252Fwww.huawei.com%252Fauth%252Faccount%252Fbase.profile%26display%3Dpage";
forumLogin(a)
});
$(".forum-login .logout-btn a").click(function(){ga("send","event","user_center","click_on_logout_tuff","header_navigation");
forumLogout()
});
$(".forum-login-app .registeredBtn").click(function(){forumMobileLogin()
});
$(".forum-login-app .app-logout-btn a").click(function(){forumMobileLogout()
});
$(".forum-login .show-logout .user-info").parent().click(function(){goAccountCenter()
});
$(".forum-home-mask .forum-home-close").click(function(){$(".forum-home-mask").hide()
});
$(".forum-home-mask .sign-button a").click(function(){if($(window).width()<1024){forumMobileLogin()
}else{var a="https://"+clientUrl+"/CAS/portal/userRegister/regbyphone.html?reqClientType="+reqClientType+"&loginChannel="+loginChannel+"&countryCode="+sysConfig.countryCode+"&lang="+sysConfig.casLangCode+"&loginUrl=https%3A%2F%2F"+clientUrl+"%2FCAS%2Fportal%2Flogin.html&service=https%3A%2F%2F"+clientLoginUrl+"%2Foauth2%2Fv2%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3D"+clientID+"%26redirect_uri%3Dhttps%253A%252F%252F"+window.location.host+"%252F"+digitalData.page.pageInfo.siteCode2+"%252Fcommunity%252Flogin%252F%26scope%3Dhttps%253A%252F%252Fwww.huawei.com%252Fauth%252Faccount%252Fbase.profile%26display%3Dpage";
forumLogin(a)
}});
$(".forum-home-mask .sign-text a").click(function(){forumLogin()
})
});
if(typeof allowHA!="undefined"&&allowHA){(function(){var n="2.1.5.301",at,c=screen.width,V=screen.height,m=1,F=false,w="",b=500,k=30*60*1000,g=location.href,ac="HW_",aq="",J=false,H=false,I="baseinfotype",G="customEvent",E="elementEvent",C="clickEvent",Z=0,Q="",an="",W=true,af=false,Y=0,S=document.referrer,h="",U="",p="",i="",D="",ar=1,f="",y="",ad="",t=false,a={},d="",aj=new Date().getTime(),ae=-1,aa="",ah="",l={},ao={},N={type:function(){var au=navigator.userAgent;
if(au.match(/AppleWebKit.*Mobile.*/)){if(au.indexOf(" wv")!==-1){return 2
}else{return 1
}}else{return 0
}}()};
_hasdk=function(){function aF(aH,aJ,aG,aI){aH?aa=aH:"";
aJ?ah=aJ:"";
aG?ao=aG:"";
aI?l.cvar=aI:"";
T(G);
return this
}function au(aH,aJ,aG,aI){aH?aa=aH:"";
aJ?ah=aJ:"";
aG?ao=aG:"";
aI?l.cvar=aI:"";
T(C);
return this
}function aE(aG){aG?d=aG:"";
return this
}function aA(aG){aG?h=aG:"";
return this
}function aw(aG){aG?U=aG:"";
return this
}function aB(aG){aG?at=aG:"";
return this
}function aC(aG){aG?i=aG:"";
return this
}function ax(aG){aG?Q=aG:"";
return this
}function az(aG){J=aG;
return this
}function aD(aG){H=aG;
return this
}function ay(aG){aG?an=aG:"";
return this
}function av(aG){aG?k=aG:"";
return this
}return{push:al,bindclick:K,sendData:aF,sendClickData:au,setOnReportUrl:aE,setTitle:aw,setUserAccount:aB,setUid:aC,setCXX:ax,setBaseinfotypeSwitch:az,setWindowCloseSwitch:aD,setSessionTimeoutDuration:av,setIdsite:ay,setPageData:aA}
}();
(function ab(){ag();
if(window.addEventListener){document.addEventListener("DOMContentLoaded",v,false)
}else{if(window.attachEvent){z()
}}})();
function z(){try{document.documentElement.doScroll("left")
}catch(au){return setTimeout(z,20)
}J?T("baseinfotype"):""
}function al(){var au,aw,av;
for(au=0;
au<arguments.length;
au+=1){av=arguments[au];
aw=av.shift();
try{if(typeof aw==="string"||aw instanceof String){_hasdk[aw].apply(_hasdk,av)
}else{aw.apply(_hasdk,av)
}}catch(ax){console.error("Invalid method:"+aw+", please check!!!")
}}return this
}function A(av){var ax=av.split("&");
for(var aw=0;
aw<ax.length;
aw++){var au=ax[aw].split("=");
if(au[0].toLocaleLowerCase()==="token".toLocaleLowerCase()){ax.splice(aw,1);
break
}}return ax.join("&")
}function ag(){ai();
Z=0;
M(window,"beforeunload",ap,false);
M(document,"visibilitychange",P)
}function P(){if(W){var au=new Date().getTime();
Z+=au-(Y||aj)
}else{Y=new Date().getTime()
}W=!W
}function ai(){!U?U=document.title:"";
p=document.title;
aq=location.host
}function v(){J?T("baseinfotype"):"";
document.removeEventListener("DOMContentLoaded",v,false)
}function o(){F=true;
var au=q(j("id"));
if(S&&!q(j("refts"))){var av=new Date().getTime();
B(j("refts"),av,180*24*60*60*1000,"/");
y=av
}else{y=q(j("refts"))
}ad=q(j("viewts"));
if(!q(j("idvc"))){B(j("idvc"),1,365*24*60*60*1000,"/")
}else{B(j("idvc"),q(j("idvc"))-0+1,365*24*60*60*1000,"/")
}ar=q(j("idvc"));
ae=0;
if(au===""||!au){var au=X(),av=new Date().getTime();
B(j("id"),au,365*24*60*60*1000,"/");
B(j("idts"),av,365*24*60*60*1000,"/");
D=av;
!at?at=au:"";
af=true
}else{D=q(j("idts"));
at?"":at=au
}O()
}function O(){f=q(j("idn"));
if(f===""||!f){f=X()
}B(j("idn"),f,k,"/")
}function x(au){var ay="";
for(var aw=0;
aw<au.length;
aw++){var av=au[aw][0];
var ax=au[aw][1];
if(ax==null){ax=""
}if(aw>0){ay+="&"
}ay=ay+av+"="+ax
}return ay
}function T(ax){if(!F){o()
}if(d===""){console.error("serverUrl is empty");
return
}if(an===""){console.error("idsite is empty");
return
}var aw=[];
a={url:A(window.location.href),title:U,at:aj,rf:A(S)};
if(ax===I){a.res=c+" X "+V;
if(ae!==-1){var az=new Date().getTime();
a.cwt=az;
a.dt=Z
}}if(ax===G||ax===C){a.en=aa;
a.el=ah;
a.cd=ao
}if(ax===E){a.ei=l.elementId===document?"#document":l.elementId;
a.ec=l.cls;
a.ps=l.position;
a.data=l.data===undefined?"":l.data;
a.cd=ao
}aw.push(["type",ax]);
aw.push(["vf",at]);
aw.push(["rt",new Date().getTime()]);
if(m===0){aw.push(["pt",encodeURIComponent(JSON.stringify(a))]);
var av=x(aw);
u(av)
}else{aw.push(["pt",a]);
O();
var ay={type:aw[0][1],vf:aw[1][1],rt:aw[2][1],ut:N.type,cxx:Q,idsite:an,suid:i,cvar:l.cvar?l.cvar:h,idts:D,idvc:ar,idn:f,refts:y,viewts:ad,hsv:n,data:aw[3][1]};
var au=R(ax)+"&idsite="+encodeURIComponent(an)+"&rec=1&r=886244&h="+new Date().getHours()+"&m="+new Date().getMinutes()+"&s="+new Date().getSeconds()+"&url="+encodeURIComponent(g)+"&_id="+encodeURIComponent(at)+"&_idts="+D+"&_idvc="+ar+"&_idn="+f+"&urlref="+S+"&_refts="+y+"&_viewts="+ad+"&scd=24&vpr="+c+" X "+V+"&cvar="+encodeURIComponent(l.cvar?l.cvar:h)+"&pdf=1&qt=0&data="+encodeURIComponent(JSON.stringify(ay));
u(au)
}}function R(av){var au="action_name="+encodeURIComponent(U);
if(av===E||av===C){au="link="+encodeURIComponent(U)
}return au
}function u(au){var av=new Image(1,1);
d?av.src=d+"?"+au:av.src="";
r()
}function r(){a={};
l={};
ao={}
}function q(av){var au=new RegExp("(^|;)[ ]*"+av+"=([^;]*)"),aw=au.exec(document.cookie);
return aw?decodeURIComponent(aw[2]):0
}function B(aA,ax,aw,az,av,ay){var au;
if(aw){au=new Date();
au.setTime(au.getTime()+aw)
}document.cookie=aA+"="+encodeURIComponent(ax)+(aw?";expires="+au.toGMTString():"")+";path="+(az||"/")+(av?";domain="+av:"")+(ay?";secure":"")
}function X(){var ax=[];
var au="0123456789abcdef";
for(var av=0;
av<36;
av++){ax[av]=au.substr(Math.floor(Math.random()*16),1)
}ax[14]="4";
ax[19]=au.substr((ax[19]&3)|8,1);
ax[8]=ax[13]=ax[18]=ax[23]="";
var aw=ax.join("");
return aw
}function j(au){return(ac+au+"_"+an+"_"+aq).replace(/\./g,"_")
}function ak(aw){var av="",au="",ay=aw.getMonth()+1,aA=aw.getDate(),aB=aw.getHours(),ax=aw.getMinutes(),aC=aw.getSeconds();
if(ay>=1&&ay<=9){ay="0"+ay
}if(aA>=0&&aA<=9){aA="0"+aA
}if(aB>=0&&aB<=9){aB="0"+aB
}if(ax>=0&&ax<=9){ax="0"+ax
}if(aC>=0&&aC<=9){aC="0"+aC
}var az=aw.getFullYear()+av+ay+av+aA+""+aB+au+ax+au+aC;
return az
}function K(au,av,aw,ay){var ax=au===document?document:document.getElementById(au);
if(ax){am(ax,aw,au,av,ay)
}return this
}function L(ay,av,ax,az,aA){var aw=window.innerHeight||document.documentElement.clientHeight||document.body.clientHeight;
var au=window.innerWidth||document.documentElement.clientWidth||document.body.clientWidth;
l.elementId=av;
l.cls=ax.className;
l.data=ay;
l.cvar=aA;
l.position={res:az.screenX+"X"+az.screenY,vpr:az.clientX+"X"+az.clientY,doc:au+"X"+aw};
T(E)
}function am(ay,ax,av,aw,az){function au(aA){L(ax,av,ay,aA,az)
}M(ay,aw,au)
}function M(aw,av,au){aw.attachEvent?aw.attachEvent("on"+av,au):aw.addEventListener(av,au,false)
}function ap(){var au,aw=new Date().getTime(),ax=aw+b;
P();
B(j("viewts"),aw,365*24*60*60*1000,"/");
H?T("baseinfotype"):"";
if(ax){var av=0;
do{au=new Date();
av++;
if(av>1000){break
}}while(au.getTime()<ax)
}}})();
if(typeof module!=="undefined"&&typeof module.exports==="object"){module.exports=_hasdk
}}(function(f){var n=function(q,p){return(q<<p)|(q>>>(32-p))
};
var a=function(u,q){var w,p,t,v,r;
t=(u&2147483648);
v=(q&2147483648);
w=(u&1073741824);
p=(q&1073741824);
r=(u&1073741823)+(q&1073741823);
if(w&p){return(r^2147483648^t^v)
}if(w|p){if(r&1073741824){return(r^3221225472^t^v)
}else{return(r^1073741824^t^v)
}}else{return(r^t^v)
}};
var o=function(p,r,q){return(p&r)|((~p)&q)
};
var m=function(p,r,q){return(p&q)|(r&(~q))
};
var k=function(p,r,q){return(p^r^q)
};
var j=function(p,r,q){return(r^(p|(~q)))
};
var h=function(r,q,w,v,p,t,u){r=a(r,a(a(o(q,w,v),p),u));
return a(n(r,t),q)
};
var c=function(r,q,w,v,p,t,u){r=a(r,a(a(m(q,w,v),p),u));
return a(n(r,t),q)
};
var i=function(r,q,w,v,p,t,u){r=a(r,a(a(k(q,w,v),p),u));
return a(n(r,t),q)
};
var d=function(r,q,w,v,p,t,u){r=a(r,a(a(j(q,w,v),p),u));
return a(n(r,t),q)
};
var g=function(t){var x;
var r=t.length;
var q=r+8;
var w=(q-(q%64))/64;
var v=(w+1)*16;
var y=Array(v-1);
var p=0;
var u=0;
while(u<r){x=(u-(u%4))/4;
p=(u%4)*8;
y[x]=(y[x]|(t.charCodeAt(u)<<p));
u++
}x=(u-(u%4))/4;
p=(u%4)*8;
y[x]=y[x]|(128<<p);
y[v-2]=r<<3;
y[v-1]=r>>>29;
return y
};
var b=function(t){var r="",p="",u,q;
for(q=0;
q<=3;
q++){u=(t>>>(q*8))&255;
p="0"+u.toString(16);
r=r+p.substr(p.length-2,2)
}return r
};
var l=function(q){q=q.replace(/\x0d\x0a/g,"\x0a");
var p="";
for(var t=0;
t<q.length;
t++){var r=q.charCodeAt(t);
if(r<128){p+=String.fromCharCode(r)
}else{if((r>127)&&(r<2048)){p+=String.fromCharCode((r>>6)|192);
p+=String.fromCharCode((r&63)|128)
}else{p+=String.fromCharCode((r>>12)|224);
p+=String.fromCharCode(((r>>6)&63)|128);
p+=String.fromCharCode((r&63)|128)
}}}return p
};
f.extend({md5:function(p){var y=Array();
var I,J,q,w,H,S,R,P,M;
var F=7,D=12,B=17,z=22;
var Q=5,N=9,L=14,K=20;
var v=4,u=11,t=16,r=23;
var G=6,E=10,C=15,A=21;
p=l(p);
y=g(p);
S=1732584193;
R=4023233417;
P=2562383102;
M=271733878;
for(I=0;
I<y.length;
I+=16){J=S;
q=R;
w=P;
H=M;
S=h(S,R,P,M,y[I+0],F,3614090360);
M=h(M,S,R,P,y[I+1],D,3905402710);
P=h(P,M,S,R,y[I+2],B,606105819);
R=h(R,P,M,S,y[I+3],z,3250441966);
S=h(S,R,P,M,y[I+4],F,4118548399);
M=h(M,S,R,P,y[I+5],D,1200080426);
P=h(P,M,S,R,y[I+6],B,2821735955);
R=h(R,P,M,S,y[I+7],z,4249261313);
S=h(S,R,P,M,y[I+8],F,1770035416);
M=h(M,S,R,P,y[I+9],D,2336552879);
P=h(P,M,S,R,y[I+10],B,4294925233);
R=h(R,P,M,S,y[I+11],z,2304563134);
S=h(S,R,P,M,y[I+12],F,1804603682);
M=h(M,S,R,P,y[I+13],D,4254626195);
P=h(P,M,S,R,y[I+14],B,2792965006);
R=h(R,P,M,S,y[I+15],z,1236535329);
S=c(S,R,P,M,y[I+1],Q,4129170786);
M=c(M,S,R,P,y[I+6],N,3225465664);
P=c(P,M,S,R,y[I+11],L,643717713);
R=c(R,P,M,S,y[I+0],K,3921069994);
S=c(S,R,P,M,y[I+5],Q,3593408605);
M=c(M,S,R,P,y[I+10],N,38016083);
P=c(P,M,S,R,y[I+15],L,3634488961);
R=c(R,P,M,S,y[I+4],K,3889429448);
S=c(S,R,P,M,y[I+9],Q,568446438);
M=c(M,S,R,P,y[I+14],N,3275163606);
P=c(P,M,S,R,y[I+3],L,4107603335);
R=c(R,P,M,S,y[I+8],K,1163531501);
S=c(S,R,P,M,y[I+13],Q,2850285829);
M=c(M,S,R,P,y[I+2],N,4243563512);
P=c(P,M,S,R,y[I+7],L,1735328473);
R=c(R,P,M,S,y[I+12],K,2368359562);
S=i(S,R,P,M,y[I+5],v,4294588738);
M=i(M,S,R,P,y[I+8],u,2272392833);
P=i(P,M,S,R,y[I+11],t,1839030562);
R=i(R,P,M,S,y[I+14],r,4259657740);
S=i(S,R,P,M,y[I+1],v,2763975236);
M=i(M,S,R,P,y[I+4],u,1272893353);
P=i(P,M,S,R,y[I+7],t,4139469664);
R=i(R,P,M,S,y[I+10],r,3200236656);
S=i(S,R,P,M,y[I+13],v,681279174);
M=i(M,S,R,P,y[I+0],u,3936430074);
P=i(P,M,S,R,y[I+3],t,3572445317);
R=i(R,P,M,S,y[I+6],r,76029189);
S=i(S,R,P,M,y[I+9],v,3654602809);
M=i(M,S,R,P,y[I+12],u,3873151461);
P=i(P,M,S,R,y[I+15],t,530742520);
R=i(R,P,M,S,y[I+2],r,3299628645);
S=d(S,R,P,M,y[I+0],G,4096336452);
M=d(M,S,R,P,y[I+7],E,1126891415);
P=d(P,M,S,R,y[I+14],C,2878612391);
R=d(R,P,M,S,y[I+5],A,4237533241);
S=d(S,R,P,M,y[I+12],G,1700485571);
M=d(M,S,R,P,y[I+3],E,2399980690);
P=d(P,M,S,R,y[I+10],C,4293915773);
R=d(R,P,M,S,y[I+1],A,2240044497);
S=d(S,R,P,M,y[I+8],G,1873313359);
M=d(M,S,R,P,y[I+15],E,4264355552);
P=d(P,M,S,R,y[I+6],C,2734768916);
R=d(R,P,M,S,y[I+13],A,1309151649);
S=d(S,R,P,M,y[I+4],G,4149444226);
M=d(M,S,R,P,y[I+11],E,3174756917);
P=d(P,M,S,R,y[I+2],C,718787259);
R=d(R,P,M,S,y[I+9],A,3951481745);
S=a(S,J);
R=a(R,q);
P=a(P,w);
M=a(M,H)
}var O=b(S)+b(R)+b(P)+b(M);
return O.toLowerCase()
}})
})(jQuery);
function getDmpaClient(){return(window.viewType()=="mobile")?"mobile":"pc"
}function getDmpaSid(){return $.md5(new Date().getTime()+""+Math.random())
}function getDmpaSite(){return window.digitalData.page.pageInfo.siteCode2.toUpperCase()
}var dmpa_site_code=window.digitalData.page.pageInfo.siteCode;
var dmpa_site_id=(dmpa_site_code=="cn")?"consumer-cn":getDmpaSite();
var dmpa_session_obj;
var dmpa_cn_site_code="cn";
var dmpa_us_site_code="us";
var nowtime=new Date().getTime();
var dmpa_sessionid;
var eVars1;
var eVars2;
var eVars3;
var eVars4;
if(checkStorageStatus()){try{dmpa_session_obj=window.localStorage.dmpa_session_obj;
if(!dmpa_session_obj||JSON.parse(localStorage.dmpa_session_obj).expires<nowtime){dmpa_sessionid=$.md5(new Date().getTime()+""+Math.random());
localStorage.setItem("dmpa_session_obj",JSON.stringify({id:dmpa_sessionid,expires:nowtime+3*30*24*3600*1000}))
}else{dmpa_sessionid=JSON.parse(localStorage.dmpa_session_obj).id
}}catch(e){dmpa_sessionid=$.md5(new Date().getTime()+""+Math.random())
}}else{dmpa_sessionid=$.md5(new Date().getTime()+""+Math.random())
}function addCcpcDmpaAnalytics(i,d,f,j,b){if(dmpa_site_code==dmpa_us_site_code){return
}if(!b){b=getDmpaSid()
}j.sid=b;
f.language=getSiteLanguage();
var a=f.keyWord||f.q;
var h="";
try{a=decodeURIComponent(a?a:"")
}catch(g){}if(f.pageNo&&f.pageNo>1){return
}var c={query:a,searchFrom:i,query_from:i,scope:d,searchParam:f,sid:b,app_id:"www-website",type:"search",action:"customSearch",language:getSiteLanguage(),site:dmpa_site_id,module:d,userId:dmpa_sessionid,site_id:dmpa_site_id,sitecode:getDmpaSite(),source:"web",languagecode:getSiteLanguage(),pageSize:f.pageSize,pageNo:f.pageNo,client:getDmpaClient()};
if(d=="global"){if(f.docCategory=="consumer_press"){c.query_doctype="press"
}else{c.query_doctype=(f.docCategory!==undefined)?"product":"support"
}}if(typeof dmpa==="function"){dmpa("setAutoSendPV",false);
dmpa("set",{siteId:"consumer-cn",user_id:""});
dmpa("setAutoLinkTracking",false)
}trackDmpaSearch(c);
trackCcpcDmpaSearchResult(b,c,j)
}function trackDmpaSearch(c){if(dmpa_site_code==dmpa_us_site_code){return
}var a=JSON.stringify(c);
try{a=decodeURIComponent(a)
}catch(b){}try{dmpa("trackEvent","customSearch",{data:"'"+a+"'"})
}catch(b){if(typeof dmpa=="function"){setTimeout(function(){dmpa("trackEvent","customSearch",{data:"'"+a+"'"})
},2000)
}}}function trackCcpcDmpaSearchResult(d,h,b){if(dmpa_site_code==dmpa_us_site_code){return
}try{var n={};
if(!b.responseCode){if(b.hits||b.relatedProds||isArrayFn(b)){n.responseCode="200";
n.responseData=b
}}else{n=b
}if(n.responseCode=="200"&&!$.isEmptyObject(n.responseData)){var c={};
if(n.responseData.hits){var j=n.responseData.hits.hits;
var a=[];
for(var k=0;
k<j.length;
k++){if(j[k]._type=="crawler"){var l=j[k]._source;
a.push({id:l.docId,title:l.dretitle})
}else{a.push({id:j[k]._id,title:j[k].highlight.title[0]})
}}c.knowList=a
}else{if(n.responseData.relatedProds){var a=[];
var g=n.responseData.relatedProds;
for(var k=0;
k<g.length;
k++){a.push({id:g[k].docId,title:g[k].dretitle})
}c.knowList=a
}else{if(n.responseData){c.knowList=n.responseData
}}}c.sid=d;
c.pageSize=h.pageSize;
c.pageNo=h.pageNo;
c.site_id=dmpa_site_id;
c.sitecode=getDmpaSite();
c.source="web";
c.app_id="www-website";
c.languagecode=getSiteLanguage();
c.scope=h.scope;
c.userId=dmpa_sessionid;
if(n.responseData&&n.responseData.interventions&&n.responseData.interventions!="undefined"){c.interventions=n.responseData.interventions
}var f=JSON.stringify(c);
try{f=decodeURIComponent(f)
}catch(m){}try{dmpa("trackEvent","display",{data:"'"+f+"'"})
}catch(m){if(typeof dmpa=="function"){setTimeout(function(){dmpa("trackEvent","display",{data:"'"+f+"'"})
},2000)
}}}}catch(m){}}function trackCcpcSearchClick(c,h,l,i,a,k,d,n){if(dmpa_site_code==dmpa_us_site_code){return
}try{var b={};
b.sid=c;
b.knowledge_context_id=h;
b.title=l;
b.index=i;
b.pageNo=a;
b.site_id=dmpa_site_id;
b.sitecode=getDmpaSite();
b.source="web";
b.app_id="www-website";
b.languagecode=getSiteLanguage();
b.userId=dmpa_sessionid;
if(d&&d!="undefined"){b.interventions=d
}if(n&&n!="undefined"){b.scope=n
}else{b.scope="service"
}if(n=="global"){if(k=="support"){k="doc";
b.query_doctype="support"
}else{b.query_doctype=(k=="product")?"product":"press"
}}else{if(k=="relatedServices"){delete b.interventions;
var g={};
try{g=JSON.parse(decodeURIComponent(d));
b.knowledge_context_id=g.card_id
}catch(j){}k="card";
b.clickFrom=h;
b.analyticsType=getAnalyticsType(h);
b.ext_data={level3:(g.level3?g.level3:"entrance")}
}else{if(k=="shop"){delete b.interventions;
var g={};
try{g=JSON.parse(decodeURIComponent(d));
b.knowledge_context_id=g.card_id
}catch(j){}k="card";
b.clickFrom=h;
b.analyticsType=getAnalyticsType("service-center");
b.ext_data={level3:"show"}
}}}var f=JSON.stringify(b);
try{f=decodeURIComponent(f)
}catch(j){}var m="";
if(k=="product"){m="clickProduct"
}else{if(k=="card"){m="expressCardClick"
}else{m="clickDoc"
}}try{dmpa("trackEvent",m,{data:"'"+f+"'"})
}catch(j){if(typeof dmpa=="function"){setTimeout(function(){dmpa("trackEvent",m,{data:"'"+f+"'"})
},2000)
}}}catch(j){}}function getVenusTimeString(){var a=new Date();
var b=a.getFullYear()+"-"+(a.getMonth()+1)+"-"+a.getDate()+" "+a.getHours()+":"+(a.getMinutes()<10?"0"+a.getMinutes():a.getMinutes())+":"+a.getSeconds();
return b
}function isArrayFn(a){if(typeof Array.isArray==="function"){return Array.isArray(a)
}else{return Object.prototype.toString.call(a)==="[object Array]"
}}function trackCcpcCardDisplay(b,k,j,l){if(dmpa_site_code==dmpa_us_site_code){return
}if(!l.responseData||l.responseData.length<0){return
}var a={};
if(j=="shop"){var c=l.responseData.extend_data.result.hits.hits;
var g=new Array();
for(var f=0;
f<c.length;
f++){if(f>2){break
}g.push({shopCode:c[f]._id,level3:"show"})
}a.custom_data=g
}else{var c=l.responseData.custom_data;
var g=new Array();
for(var f=0;
f<c.length;
f++){if(f>2){break
}g.push({card_id:c[f].card_id,level3:(c[f].level3?c[f].level3:"entrance")})
}a.custom_data=g
}a.type="card";
a.displayFrom=j;
a.sid=b;
a.site_id=dmpa_site_id;
a.sitecode=getDmpaSite();
a.source="web";
a.app_id="www-website";
a.languagecode=getSiteLanguage();
a.scope=k;
a.userId=dmpa_sessionid;
var d=JSON.stringify(a);
try{d=decodeURIComponent(d);
if(typeof dmpa==="function"){dmpa("setAutoSendPV",false);
dmpa("set",{siteId:"consumer-cn",user_id:""});
dmpa("setAutoLinkTracking",false);
dmpa("trackEvent","cardInfoDisplay",{data:"'"+d+"'"})
}}catch(h){}}function getAnalyticsType(b){var a="";
switch(b.toLocaleLowerCase()){case"express-repair":a="function";
break;
case"reservation":a="function";
break;
case"door-to-door-service":a="function";
break;
case"sparepart-price":a="function";
break;
case"inquiry":a="function";
break;
case"service-center":a="shop";
break;
case"warranty-query":a="function";
break;
case"vipservice":a="function";
break;
case"hicare":a="software";
break;
case"hisuite":a="software";
break;
case"phone clone":a="software";
break;
case"app store":a="software";
break;
case"beta":a="software";
break;
case"hotline":a="hotline";
break;
case"email feedback":a="email";
break;
case"activities":a="activities";
break;
case"roaming":a="function";
break;
case"honor":a="honor";
break;
default:a="function"
}return a
}function getGAData(d){if(!d){return null
}var a=d.split(" - ");
var c=queryVariableD(a[0]);
for(var b=1;
b<a.length;
b++){c=c+" - "+queryVariableD(a[b])
}return c
}window.variableTagD={"<page title>":digitalData.page.pageInfo.pageName,"<URL>":digitalData.page.pageInfo.uri,"<product name>":digitalData.product?digitalData.product.productInfo.marketingName:""};
window.queryVariableD=function(f){var a=window.variableTagD;
var d=f;
var c=/^<.*>$/;
for(var b in a){if(b==f){d=a[b]
}}if(c.test(d)){d=""
}return d
};
function sendDmpaByAttr(c,g,f,d,j,a,b){var c=c?c:"click";
var d=d?getGAData(d):"Error: Not Maintain Value";
var h=f?getGAData(f):"Error: Not Maintain Value";
var g=g?getGAData(g):"Error: Not Maintain Value";
g=g+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var j=j?j:null;
var a=a?a:null;
var b=b?b:null;
var i={category:g,label:d,value:h,location:window.location.href,uri:window.digitalData.page.pageInfo.uri,subModuleName:"Support"};
if(j!=null){i.QueryResult=j
}if(a!=null){i.SearchPageNum=a
}if(b!=null){i.ProductName=b
}if(typeof dmpa5==="function"){dmpa5("trackEvent",c,i)
}}function sendDmpaByAttr2(f,j,i,h,m,c,d,b,a,g){var f=f?f:"click";
var h=h?getGAData(h):"Error: Not Maintain Value";
var k=i?getGAData(i):"Error: Not Maintain Value";
var j=j?getGAData(j):"Error: Not Maintain Value";
j=j+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var m=m?m:null;
var c=c?c:null;
var d=d?d:null;
var b=b?b:null;
var a=a?a:null;
var g=g?g:null;
var l={category:j,label:h,value:k,location:window.location.href,uri:window.digitalData.page.pageInfo.uri,subModuleName:"Support"};
if(m!=null){l.QueryResult=m
}if(c!=null){l.SearchPageNum=c
}if(d!=null){l.ProductName=d
}if(b!=null){l.FAQViewTime=b
}if(a!=null){l.FAQChannelEntrance=a
}if(g!=null){l.FAQParameter=g
}if(typeof dmpa5==="function"){dmpa5("trackEvent",f,l)
}}function sendDmpaByAttr3(f,k,j,i,n,c,d,b,a,h,g){var f=f?f:"click";
var i=i?getGAData(i):"Error: Not Maintain Value";
var l=j?getGAData(j):"Error: Not Maintain Value";
var k=k?getGAData(k):"Error: Not Maintain Value";
k=k+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var n=n?n:null;
var c=c?c:null;
var d=d?d:null;
var b=b?b:null;
var a=a?a:null;
var h=h?h:null;
var g=g?g:null;
var m={category:k,label:i,value:l,location:window.location.href,uri:window.digitalData.page.pageInfo.uri,subModuleName:"Support"};
if(n!=null){m.QueryResult=n
}if(c!=null){m.SearchPageNum=c
}if(d!=null){m.ProductName=d
}if(b!=null){m.FAQViewTime=b
}if(a!=null){m.FAQChannelEntrance=a
}if(h!=null){m.FAQParameter=h
}if(g!=null){m.ContentTitle=g
}if(typeof dmpa5==="function"){dmpa5("trackEvent",f,m)
}}function sendDmpaByData(d){var c=d.eType?d.eType:"click";
var f=d.label?getGAData(d.label):"Error: Not Maintain Value";
var h=d.value?getGAData(d.value):"Error: Not Maintain Value";
var g=d.category?getGAData(d.category):"Error: Not Maintain Value";
g=g+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var j=d.QueryResult?d.QueryResult:null;
var a=d.SearchPageNum?d.SearchPageNum:null;
var b=d.ProductName?d.ProductName:null;
var i={category:g,label:f,value:h,location:window.location.href,uri:window.digitalData.page.pageInfo.uri,subModuleName:"Support"};
if(j!=null){i.QueryResult=j
}if(a!=null){i.SearchPageNum=a
}if(b!=null){i.ProductName=b
}if(typeof dmpa5==="function"){dmpa5("trackEvent",c,i)
}}function sendDmpaByCurrentTag(j){var a=window.event;
if(!a||!a.isTrusted||$(a.target).closest($(j)).length<1){return
}var d=$(j).attr("dmpa-etype")?$(j).attr("dmpa-etype"):"click";
var f=$(j).attr("lab")?getGAData($(j).attr("lab")):"Error: Not Maintain Value";
var h=$(j).attr("act")?getGAData($(j).attr("act")):"Error: Not Maintain Value";
var g=$(j).attr("cat")?getGAData($(j).attr("cat")):"Error: Not Maintain Value";
g=g+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var k=$(j).attr("queryresult")?$(j).attr("queryresult"):null;
var b=$(j).attr("searchpagenum")?$(j).attr("searchpagenum"):null;
var c=$(j).attr("productname")?$(j).attr("productname"):null;
var i={category:g,label:f,value:h,location:window.location.href,uri:window.digitalData.page.pageInfo.uri,subModuleName:"Support"};
if(k!=null){i.QueryResult=k
}if(b!=null){i.SearchPageNum=b
}if(c!=null){i.ProductName=c
}if(typeof dmpa5==="function"){dmpa5("trackEvent",d,i)
}}function sendDmpaByClass(a){if(!a||!a.originalEvent||!a.originalEvent.isTrusted){return
}var d=$(this).attr("dmpa-etype")?$(this).attr("dmpa-etype"):"click";
var f=$(this).attr("lab")?getGAData($(this).attr("lab")):"Error: Not Maintain Value";
var h=$(this).attr("act")?getGAData($(this).attr("act")):"Error: Not Maintain Value";
var g=$(this).attr("cat")?getGAData($(this).attr("cat")):"Error: Not Maintain Value";
g=g+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var j=$(this).attr("queryresult")?$(this).attr("queryresult"):null;
var b=$(this).attr("searchpagenum")?$(this).attr("searchpagenum"):null;
var c=$(this).attr("productname")?$(this).attr("productname"):null;
var i={category:g,label:f,value:h,location:window.location.href,uri:window.digitalData.page.pageInfo.uri,subModuleName:"Support"};
if(j!=null){i.QueryResult=j
}if(b!=null){i.SearchPageNum=b
}if(c!=null){i.ProductName=c
}if(typeof dmpa5==="function"){dmpa5("trackEvent",d,i)
}}$(document).on("click",".dmpa-click-dispach",sendDmpaByClass);
function gaAndAaByAttr3(k,j,i,l,c,f,b,a,h,g,d){var i=i?getGAData(i):"Error: Not Maintain Value";
var j=j?getGAData(j):"Error: Not Maintain Value";
var k=k?getGAData(k):"Error: Not Maintain Value";
k=k+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var l=l?l:null;
var c=c?c:null;
var f=f?f:null;
var b=b?b:null;
var a=a?a:null;
var h=h?h:null;
var g=g?g:null;
var d=d?d:null;
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",k,j,i,{dimension7:l,dimension8:c,dimension9:f,dimension10:b,dimension11:a,dimension12:h,dimension13:g,dimension16:d});
ga("send","event",k,j,i)
}}function gaAndAaByAttr2(j,i,h,k,c,f,b,a,g,d){var h=h?getGAData(h):"Error: Not Maintain Value";
var i=i?getGAData(i):"Error: Not Maintain Value";
var j=j?getGAData(j):"Error: Not Maintain Value";
j=j+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var k=k?k:null;
var c=c?c:null;
var f=f?f:null;
var b=b?b:null;
var a=a?a:null;
var g=g?g:null;
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",j,i,h,{nonInteraction:true,dimension7:k,dimension8:c,dimension9:f,dimension10:b,dimension11:a,dimension12:g,dimension14:d});
ga("send","event",j,i,h)
}}function gaAndAaByAttr(b,d,f,a,c,h){var f=f?getGAData(f):"Error: Not Maintain Value";
var d=d?getGAData(d):"Error: Not Maintain Value";
var b=b?getGAData(b):"Error: Not Maintain Value";
b=b+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var a=a?a:null;
var c=c?c:null;
var h=h?h:null;
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",b,d,f,{dimension7:a,dimension8:c,dimension9:h});
ga("send","event",b,d,f)
}var g={};
g.customEventType="aSupportCommonClick";
g.sid=$.md5(new Date().getTime()+""+Math.random());
g.cat=b==undefined||b==null?"":decodeURIComponent(b);
g.act=d==undefined||d==null?"":decodeURIComponent(d);
g.lab=f==undefined||f==null?"":decodeURIComponent(f.replace(/%/g,"%25"));
g.QueryResult=a==undefined||a==null?"":decodeURIComponent(a);
g.SearchPageNum=c==undefined||c==null?"":decodeURIComponent(c);
g.ProductName=h==undefined||h==null?"":decodeURIComponent(h)
}function gaAndAaByCurrentTag(i){var a=window.event;
if(!a||!a.isTrusted||$(a.target).closest($(i)).length<1){return
}var f=$(i).attr("lab")?getGAData($(i).attr("lab")):"Error: Not Maintain Value";
var g=$(i).attr("act")?getGAData($(i).attr("act")):"Error: Not Maintain Value";
var h=$(i).attr("cat")?getGAData($(i).attr("cat")):"Error: Not Maintain Value";
h=h+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var j=$(i).attr("queryresult")?$(i).attr("queryresult"):null;
var b=$(i).attr("searchpagenum")?$(i).attr("searchpagenum"):null;
var c=$(i).attr("productname")?$(i).attr("productname"):null;
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",h,g,f,{dimension7:j,dimension8:b,dimension9:c});
ga("send","event",h,g,f)
}var d={};
d.customEventType="aSupportCommonClick";
d.sid=$.md5(new Date().getTime()+""+Math.random());
d.cat=h==undefined||h==null?"":decodeURIComponent(h);
d.act=g==undefined||g==null?"":decodeURIComponent(g);
d.lab=f==undefined||f==null?"":decodeURIComponent(f);
d.QueryResult=j==undefined||j==null?"":decodeURIComponent(j);
d.SearchPageNum=b==undefined||b==null?"":decodeURIComponent(b);
d.ProductName=c==undefined||c==null?"":decodeURIComponent(c)
}function gaAndAabyASupportCommon(g){if(!g||!g.originalEvent||!g.originalEvent.isTrusted){return
}var f=$(this).attr("lab")?getGAData($(this).attr("lab")):"Error: Not Maintain Value";
var d=$(this).attr("act")?getGAData($(this).attr("act")):"Error: Not Maintain Value";
var b=$(this).attr("cat")?getGAData($(this).attr("cat")):"Error: Not Maintain Value";
b=b+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var a=$(this).attr("queryresult")?$(this).attr("queryresult"):null;
var c=$(this).attr("searchpagenum")?$(this).attr("searchpagenum"):null;
var i=$(this).attr("productname")?$(this).attr("productname"):null;
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",b,d,f,{dimension7:a,dimension8:c,dimension9:i});
ga("send","event",b,d,f)
}var h={};
h.customEventType="aSupportCommonClick";
h.sid=$.md5(new Date().getTime()+""+Math.random());
h.cat=b==undefined||b==null?"":decodeURIComponent(b);
h.act=d==undefined||d==null?"":decodeURIComponent(d);
h.lab=f==undefined||f==null?"":decodeURIComponent(f);
h.QueryResult=a==undefined||a==null?"":decodeURIComponent(a);
h.SearchPageNum=c==undefined||c==null?"":decodeURIComponent(c);
h.ProductName=i==undefined||i==null?"":decodeURIComponent(i)
}$(document).on("click",".a-support-common",gaAndAabyASupportCommon);
function sendPageViewGA(b){if(typeof ga==="function"){var c=window.digitalData.page.pageInfo.uri;
if(c!=""&&(c.lastIndexOf("/")==c.length-1)){c=c.substr(0,c.length-1)
}var a=c+b;
ga("newhuaiweisupport.send","pageview",a)
}}function sendPageViewGAByTag(a){var b=$(a).attr("ga-path")?$(a).attr("ga-path"):null;
sendPageViewGA(b)
}function sendPageViewGAByThis(){var a=$(this).attr("ga-path")?$(this).attr("ga-path"):null;
sendPageViewGA(a)
}$(document).on("click",".ga-page-view",sendPageViewGAByThis);
function initHaEnvironment(c,g){var d=document.domain;
var b="";
var a=window.digitalData.page.pageInfo.siteCode;
if(d=="consumer.huawei.com"){if(g.China.sites.hasOwnProperty(a)){b=g.China.url
}else{if(g.Russia.sites.hasOwnProperty(countryCode)){b=g.Russia.url
}else{if(g.Europe.sites.hasOwnProperty(countryCode)){b=g.Europe.url
}else{if(g.Singapore.sites.hasOwnProperty(countryCode)){b=g.Singapore.url
}}}}}else{b=g.test.url
}c.setOnReportUrl(b);
c.setIdsite("huawei_website_20191106");
c.setBaseinfotypeSwitch(false);
c.setWindowCloseSwitch(false);
var f=document.title;
c.setTitle(f);
c.setCXX(sysConfig.countryCode);
c.setUid("acf0c6ba42h")
}var haURLsJson={test:{url:"https://cloudbackup.hwcloudtest.cn:6447/webv1"},China:{url:"https://metrics-drcn.dt.hicloud.com/webv1",sites:{en:"",cn:""}},Russia:{url:"https://metrics5.data.hicloud.com:6447/webv1",sites:{ru:""}},Europe:{url:"https://metrics2.data.hicloud.com:6447/webv1",sites:{at:"",by:"",be:"",ba:"",br:"",bg:"",hr:"",cy:"",cz:"",dk:"",ee:"",fi:"",fr:"",de:"",gr:"",hu:"",ie:"",it:"",jp:"",kr:"",lv:"",lt:"",md:"",nl:"",mk:"",no:"",pl:"",pt:"",ro:"",rs:"",sk:"",si:"",es:"",se:"",ch:"",tr:"",ua:"",uk:"",us:"","us-es":"","ch-fr":"","md-ru":"","be-fr":"","lv-ru":""}},Singapore:{url:"https://metrics-dra.dt.hicloud.com:6447/webv1",sites:{dz:"",ar:"",az:"",bd:"",bo:"",bw:"",kh:"",cm:"",ca:"","ca-fr":"",cl:"",co:"",cg:"",cr:"","do":"",ec:"",eg:"","eg-e":"","et-en":"",gh:"",gt:"",hk:"","in":"",id:"",ir:"","ir-fa":"",il:"",kz:"",ke:"",kw:"","kw-en":"",la:"",latin:"","latin-en":"",levant:"","levant-ar":"",my:"",mu:"",mx:"",ma:"",mm:"",np:"",nz:"",ng:"",pk:"",pa:"",py:"",pe:"",ph:"",sa:"","sa-en":"",sg:"",za:"",lk:"",tw:"",th:"",tg:"",tn:"",ae:"","ae-fa":"",uy:"",uz:"",vn:""}}};
function sendPageHAEvent(){var a={};
a.languagecode=sysConfig.language;
a.countrycode=sysConfig.countryCode;
a.id="page_event_"+sysConfig.countryCode;
a.pageID=window.digitalData.page.pageInfo.pageName;
a.url=document.location.pathname;
if(haSdk!=undefined&&haSdk!=null&&window.digitalData.page.category.pageType=="support"){haSdk.sendData(a.id,a.id,a)
}}try{if(allowHA){var haSdk=_hasdk||[];
initHaEnvironment(haSdk,haURLsJson);
sendPageHAEvent()
}}catch(e){}function sendHa(a){if(haSdk!=undefined&&haSdk!=null&&allowHA){haSdk.sendData(a.id,a.id,a)
}}function haDispach(a){a.languagecode=sysConfig.language;
a.countrycode=sysConfig.countryCode;
console.log("HA --------------------------------------------");
console.log(a);
sendHa(a)
}function haDispachByThis(){var t={};
t.languagecode=sysConfig.language;
t.countrycode=sysConfig.countryCode;
var k=$(this).attr("ha-id")?$(this).attr("ha-id"):null;
if(k!=null){t.id=k
}var d=$(this).attr("ha-url")?$(this).attr("ha-url"):null;
if(d!=null){t.url=d
}var c=$(this).attr("ha-type")?$(this).attr("ha-type"):null;
if(c!=null){t.type=c
}var u=$(this).attr("ha-title")?$(this).attr("ha-title"):null;
if(u!=null){t.title=u
}var f=$(this).attr("ha-time")?$(this).attr("ha-time"):null;
if(f!=null){t.time=f
}var i=$(this).attr("ha-result")?$(this).attr("ha-result"):null;
if(i!=null){t.result=i
}var b=$(this).attr("ha-province")?$(this).attr("ha-province"):null;
if(b!=null){t.province=b
}var r=$(this).attr("ha-position")?$(this).attr("ha-position"):null;
if(r!=null){t.position=r
}var v=$(this).attr("ha-name")?$(this).attr("ha-name"):null;
if(v!=null){t.name=v
}var q=$(this).attr("ha-keyword")?$(this).attr("ha-keyword"):null;
if(q!=null){t.keyword=q
}var p=$(this).attr("ha-date")?$(this).attr("ha-date"):null;
if(p!=null){t.date=p
}var j=$(this).attr("ha-cycle")?$(this).attr("ha-cycle"):null;
if(j!=null){t.cycle=j
}var m=$(this).attr("ha-content")?$(this).attr("ha-content"):null;
if(m!=null){t.content=m
}var g=$(this).attr("ha-confirm")?$(this).attr("ha-confirm"):null;
if(g!=null){t.confirm=g
}var n=$(this).attr("ha-city")?$(this).attr("ha-city"):null;
if(n!=null){t.city=n
}var l=$(this).attr("ha-cat")?$(this).attr("ha-cat"):null;
if(l!=null){t.category=l
}var o=$(this).attr("ha-area")?$(this).attr("ha-area"):null;
if(o!=null){t.area=o
}var a=$(this).attr("ha-duration")?$(this).attr("ha-duration"):null;
if(a!=null){t.duration=a
}var h=$(this).attr("ha-street")?$(this).attr("ha-street"):null;
if(h!=null){t.street=h
}sendHa(t)
}function haDispachByTag(u){var t={};
t.languagecode=sysConfig.language;
t.countrycode=sysConfig.countryCode;
var k=$(u).attr("ha-id")?$(u).attr("ha-id"):null;
if(k!=null){t.id=k
}var d=$(u).attr("ha-url")?$(u).attr("ha-url"):null;
if(d!=null){t.url=k
}var c=$(u).attr("ha-type")?$(u).attr("ha-type"):null;
if(c!=null){t.type=c
}var v=$(u).attr("ha-title")?$(u).attr("ha-title"):null;
if(v!=null){t.title=v
}var f=$(u).attr("ha-time")?$(u).attr("ha-time"):null;
if(f!=null){t.time=f
}var i=$(u).attr("ha-result")?$(u).attr("ha-result"):null;
if(i!=null){t.result=i
}var b=$(u).attr("ha-province")?$(u).attr("ha-province"):null;
if(b!=null){t.province=b
}var r=$(u).attr("ha-position")?$(u).attr("ha-position"):null;
if(r!=null){t.position=r
}var w=$(u).attr("ha-name")?$(u).attr("ha-name"):null;
if(w!=null){t.name=w
}var q=$(u).attr("ha-keyword")?$(u).attr("ha-keyword"):null;
if(q!=null){t.keyword=q
}var p=$(u).attr("ha-date")?$(u).attr("ha-date"):null;
if(p!=null){t.date=p
}var j=$(u).attr("ha-cycle")?$(u).attr("ha-cycle"):null;
if(j!=null){t.cycle=j
}var m=$(u).attr("ha-content")?$(u).attr("ha-content"):null;
if(m!=null){t.content=m
}var g=$(u).attr("ha-confirm")?$(u).attr("ha-confirm"):null;
if(g!=null){t.confirm=g
}var n=$(u).attr("ha-city")?$(u).attr("ha-city"):null;
if(n!=null){t.city=n
}var l=$(u).attr("ha-cat")?$(u).attr("ha-cat"):null;
if(l!=null){t.category=l
}var o=$(u).attr("ha-area")?$(u).attr("ha-area"):null;
if(o!=null){t.area=o
}var a=$(u).attr("ha-duration")?$(u).attr("ha-duration"):null;
if(a!=null){t.duration=a
}var h=$(u).attr("ha-street")?$(u).attr("ha-street"):null;
if(h!=null){t.street=h
}sendHa(t)
}$(document).on("click",".ha-click-dispach",haDispachByThis);
function dmpaDateFormat(d,a){var c={"M+":d.getMonth()+1,"d+":d.getDate(),"h+":d.getHours(),"m+":d.getMinutes(),"s+":d.getSeconds(),"q+":Math.floor((d.getMonth()+3)/3),S:d.getMilliseconds()};
if(/(y+)/.test(a)){a=a.replace(RegExp.$1,(d.getFullYear()+"").substr(4-RegExp.$1.length))
}for(var b in c){if(new RegExp("("+b+")").test(a)){a=a.replace(RegExp.$1,RegExp.$1.length==1?c[b]:("00"+c[b]).substr((""+c[b]).length))
}}return a
}function timeConversion(f){var h=(-1)*new Date().getTimezoneOffset()/60;
var c=h*60*60*1000;
var b=(f.substring(0,19)).replace(/-/g,"/");
var a=new Date(b).getTime()+c;
var g=h;
if(window.sessionStorage.getItem("timeZoneOffeset")!=null){g=window.sessionStorage.getItem("timeZoneOffeset")
}var d=a+(g-h)*60*60*1000;
return dmpaDateFormat(new Date(d),"yyyy-MM-dd hh:mm:ss")
}function getVenusSearchType(a){if(!a){a=getUrlParam("t")
}var b="";
if(a=="PopupHotSearch"||a=="HotSearch"){b="hotSearch"
}else{if(a=="PopupSuggestSearch"||a=="SearchSuggest"){b="completeSearch"
}else{b="searchClick"
}}return b
}function checkIsUrgent(){var c=$(".product-urgent-download").is(":checked");
var b="product";
var d="Click on software search";
var f="";
if(c){f="open"
}else{f="close"
}var g="product_click_emergency_download";
var a={id:g,ha_confirm:f};
haDispach(a);
gaAndAaByAttr(b,d,f,"","","")
}function deviceType(){var a=window.innerWidth||$(window).width();
return a>=1024?"pc":(a<768?"mobile":"tablet")
}if(typeof pageCategory!="undefined"&&pageCategory=="support"){var cat="scroll";
var value=(deviceType()=="pc"?"Desktop":deviceType())+" scroll";
var gaHACat=value+"+"+sysConfig.countryCode+"+"+sysConfig.language;
var lab=window.location.pathname;
var roll_25=0,roll_50=0,roll_75=0,roll_100=0,gaScrollPercent=0;
$(document).on("scroll",function(){gaScrollPercent=getCookie("scrollPercentage")||0;
if(gaScrollPercent>24&&gaScrollPercent<49&&roll_25==0){roll_25=1;
var b="Content 25%";
sendDmpaByAttr("scroll",cat,value,b);
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",gaHACat,b,lab,{nonInteraction:true});
ga("send","event",gaHACat,b,lab,{nonInteraction:true})
}var a={id:"content_scroll",title:"25%"};
haDispach(a)
}if(gaScrollPercent>49&&gaScrollPercent<74&&roll_50==0){roll_50=1;
sendDmpaByAttr("scroll",cat,value,"Content 50%");
var b="Content 50%";
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",gaHACat,b,lab,{nonInteraction:true});
ga("send","event",gaHACat,b,lab,{nonInteraction:true})
}var a={id:"content_scroll",title:"50%"};
haDispach(a)
}if(gaScrollPercent>74&&gaScrollPercent<99&&roll_75==0){roll_75=1;
sendDmpaByAttr("scroll",cat,value,"Content 75%");
var b="Content 75%";
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",gaHACat,b,lab,{nonInteraction:true});
ga("send","event",gaHACat,b,lab,{nonInteraction:true})
}var a={id:"content_scroll",title:"75%"};
haDispach(a)
}if(gaScrollPercent==100&&roll_100==0){roll_100=1;
var b="Content 100%";
sendDmpaByAttr("scroll",cat,value,b);
if(typeof ga==="function"){ga("newhuaiweisupport.send","event",gaHACat,b,lab,{nonInteraction:true});
ga("send","event",gaHACat,b,lab,{nonInteraction:true})
}var a={id:"content_scroll",title:"100%"};
haDispach(a)
}})
}"undefined"==typeof jwplayer&&(jwplayer=function(b){if(jwplayer.api){return jwplayer.api.selectPlayer(b)
}},jwplayer.version="6.6.3896",jwplayer.vid=document.createElement("video"),jwplayer.audio=document.createElement("audio"),jwplayer.source=document.createElement("source"),function(b){function n(g){return function(){return a(g)
}
}function j(g){return function(){g("Error loading file")
}
}function d(g,m,i,l){return function(){try{var p=g.responseXML;
if(p&&p.firstChild){return i(g)
}}catch(o){}(p=v.parseXML(g.responseText))&&p.firstChild?(g=v.extend({},g,{responseXML:p}),i(g)):l&&l(g.responseText?"Invalid XML":m)
}
}var f=document,c=window,h=navigator,v=b.utils=function(){};
v.exists=function(g){switch(typeof g){case"string":return 0<g.length;
case"object":return null!==g;
case"undefined":return !1
}return !0
};
v.styleDimension=function(g){return g+(0<g.toString().indexOf("%")?"":"px")
};
v.getAbsolutePath=function(g,m){v.exists(m)||(m=f.location.href);
if(v.exists(g)){var i;
if(v.exists(g)){i=g.indexOf("://");
var l=g.indexOf("?");
i=0<i&&(0>l||l>i)
}else{i=void 0
}if(i){return g
}i=m.substring(0,m.indexOf("://")+3);
var l=m.substring(i.length,m.indexOf("/",i.length+1)),p;
0===g.indexOf("/")?p=g.split("/"):(p=m.split("?")[0],p=p.substring(i.length+l.length+1,p.lastIndexOf("/")),p=p.split("/").concat(g.split("/")));
for(var q=[],o=0;
o<p.length;
o++){p[o]&&(v.exists(p[o])&&"."!=p[o])&&(".."==p[o]?q.pop():q.push(p[o]))
}return i+l+"/"+q.join("/")
}};
v.extend=function(){var g=v.extend.arguments;
if(1<g.length){for(var i=1;
i<g.length;
i++){v.foreach(g[i],function(o,l){try{v.exists(l)&&(g[0][o]=l)
}catch(m){}})
}return g[0]
}return null
};
v.log=function(i,g){"undefined"!=typeof console&&"undefined"!=typeof console.log&&(g?console.log(i,g):console.log(i))
};
var a=v.userAgentMatch=function(g){return null!==h.userAgent.toLowerCase().match(g)
};
v.isIE=n(/msie/i);
v.isFF=n(/firefox/i);
v.isChrome=n(/chrome/i);
v.isIOS=n(/iP(hone|ad|od)/i);
v.isIPod=n(/iP(hone|od)/i);
v.isIPad=n(/iPad/i);
v.isSafari602=n(/Macintosh.*Mac OS X 10_8.*6\.0\.\d* Safari/i);
v.isSafari=function(){return a(/safari/i)&&!a(/chrome/i)&&!a(/chromium/i)&&!a(/android/i)
};
v.isAndroid=function(g){return g?a(RegExp("android.*"+g,"i")):a(/android/i)
};
v.isMobile=function(){return v.isIOS()||v.isAndroid()
};
v.saveCookie=function(i,g){f.cookie="jwplayer."+i+"\x3d"+g+"; path\x3d/"
};
v.getCookies=function(){for(var m={},l=f.cookie.split("; "),g=0;
g<l.length;
g++){var i=l[g].split("\x3d");
0==i[0].indexOf("jwplayer.")&&(m[i[0].substring(9,i[0].length)]=i[1])
}return m
};
v.typeOf=function(i){var g=typeof i;
return"object"===g?!i?"null":i instanceof Array?"array":g:g
};
v.translateEventResponse=function(g,l){var i=v.extend({},l);
g==b.events.JWPLAYER_FULLSCREEN&&!i.fullscreen?(i.fullscreen="true"==i.message?!0:!1,delete i.message):"object"==typeof i.data?(i=v.extend(i,i.data),delete i.data):"object"==typeof i.metadata&&v.deepReplaceKeyName(i.metadata,["__dot__","__spc__","__dsh__","__default__"],["."," ","-","default"]);
v.foreach(["position","duration","offset"],function(o,m){i[m]&&(i[m]=Math.round(1000*i[m])/1000)
});
return i
};
v.flashVersion=function(){if(v.isAndroid()){return 0
}var g=h.plugins,i;
try{if("undefined"!==g&&(i=g["Shockwave Flash"])){return parseInt(i.description.replace(/\D+(\d+)\..*/,"$1"))
}}catch(l){}if("undefined"!=typeof c.ActiveXObject){try{if(i=new ActiveXObject("ShockwaveFlash.ShockwaveFlash")){return parseInt(i.GetVariable("$version").split(" ")[1].split(",")[0])
}}catch(m){}}return 0
};
v.getScriptPath=function(m){for(var l=f.getElementsByTagName("script"),g=0;
g<l.length;
g++){var i=l[g].src;
if(i&&0<=i.indexOf(m)){return i.substr(0,i.indexOf(m))
}}return""
};
v.deepReplaceKeyName=function(g,i,l){switch(b.utils.typeOf(g)){case"array":for(var m=0;
m<g.length;
m++){g[m]=b.utils.deepReplaceKeyName(g[m],i,l)
}break;
case"object":v.foreach(g,function(o,p){var t;
if(i instanceof Array&&l instanceof Array){if(i.length!=l.length){return
}t=i
}else{t=[i]
}for(var r=o,q=0;
q<t.length;
q++){r=r.replace(RegExp(i[q],"g"),l[q])
}g[r]=b.utils.deepReplaceKeyName(p,i,l);
o!=r&&delete g[o]
})
}return g
};
var k=v.pluginPathType={ABSOLUTE:0,RELATIVE:1,CDN:2};
v.getPluginPathType=function(g){if("string"==typeof g){g=g.split("?")[0];
var i=g.indexOf("://");
if(0<i){return k.ABSOLUTE
}var l=g.indexOf("/");
g=v.extension(g);
return 0>i&&0>l&&(!g||!isNaN(g))?k.CDN:k.RELATIVE
}};
v.getPluginName=function(g){return g.replace(/^(.*\/)?([^-]*)-?.*\.(swf|js)$/,"$2")
};
v.getPluginVersion=function(g){return g.replace(/[^-]*-?([^\.]*).*$/,"$1")
};
v.isYouTube=function(g){return/^(http|\/\/).*(youtube\.com|youtu\.be)\/.+/.test(g)
};
v.youTubeID=function(i){try{return/v[=\/]([^?&]*)|youtu\.be\/([^?]*)|^([\w-]*)$/i.exec(i).slice(1).join("").replace("?","")
}catch(g){return""
}};
v.isRtmp=function(i,g){return 0==i.indexOf("rtmp")||"rtmp"==g
};
v.foreach=function(g,i){var l,m;
for(l in g){"function"==v.typeOf(g.hasOwnProperty)?g.hasOwnProperty(l)&&(m=g[l],i(l,m)):(m=g[l],i(l,m))
}};
v.isHTTPS=function(){return 0==c.location.href.indexOf("https")
};
v.repo=function(){var g="http://consumer-res.huawei.com/etc/designs/huawei-cbg-site/statics/";
try{v.isHTTPS()&&(g=g.replace("http://","https://"))
}catch(i){}return g
};
v.ajax=function(i,r,q){var o;
0<i.indexOf("#")&&(i=i.replace(/#.*$/,""));
var m;
m=(m=i)&&0<=m.indexOf("://")&&m.split("/")[2]!=c.location.href.split("/")[2]?!0:!1;
if(m&&v.exists(c.XDomainRequest)){o=new XDomainRequest,o.onload=d(o,i,r,q),o.onerror=j(q,i,o)
}else{if(v.exists(c.XMLHttpRequest)){var l=o=new XMLHttpRequest,p=i;
o.onreadystatechange=function(){if(4===l.readyState){switch(l.status){case 200:d(l,p,r,q)();
break;
case 404:q("File not found")
}}};
o.onerror=j(q,i)
}else{q&&q()
}}try{o.open("GET",i,!0),o.send(null)
}catch(g){q&&q(i)
}return o
};
v.parseXML=function(m){try{var l;
if(c.DOMParser){l=(new DOMParser).parseFromString(m,"text/xml");
try{if("parsererror"==l.childNodes[0].firstChild.nodeName){return
}}catch(g){}}else{l=new ActiveXObject("Microsoft.XMLDOM"),l.async="false",l.loadXML(m)
}return l
}catch(i){}};
v.filterPlaylist=function(i,g){for(var l=[],q=0;
q<i.length;
q++){var p=v.extend({},i[q]);
p.sources=v.filterSources(p.sources);
if(0<p.sources.length){for(var o=0;
o<p.sources.length;
o++){var m=p.sources[o];
m.label||(m.label=o.toString())
}l.push(p)
}}if(g&&0==l.length){for(q=0;
q<i.length;
q++){if(p=v.extend({},i[q]),p.sources=v.filterSources(p.sources,!0),0<p.sources.length){for(o=0;
o<p.sources.length;
o++){m=p.sources[o],m.label||(m.label=o.toString())
}l.push(p)
}}}return l
};
v.filterSources=function(i,q){var g,o,p=v.extensionmap;
if(i){o=[];
for(var l=0;
l<i.length;
l++){var m=i[l].type,r=i[l].file;
r&&r.trim&&(r=r.trim());
m||(m=p.extType(v.extension(r)),i[l].type=m);
q?b.embed.flashCanPlay(r,m)&&(g||(g=m),m==g&&o.push(v.extend({},i[l]))):v.canPlayHTML5(m)&&(g||(g=m),m==g&&o.push(v.extend({},i[l])))
}}return o
};
v.canPlayHTML5=function(g){if(v.isAndroid()&&("hls"==g||"m3u"==g||"m3u8"==g)){return !1
}g=v.extensionmap.types[g];
return !!g&&!!b.vid.canPlayType&&b.vid.canPlayType(g)
};
v.seconds=function(i){i=i.replace(",",".");
var l=i.split(":"),g=0;
"s"==i.substr(-1)?g=Number(i.substr(0,i.length-1)):"m"==i.substr(-1)?g=60*Number(i.substr(0,i.length-1)):"h"==i.substr(-1)?g=3600*Number(i.substr(0,i.length-1)):1<l.length?(g=Number(l[l.length-1]),g+=60*Number(l[l.length-2]),3==l.length&&(g+=3600*Number(l[l.length-3]))):g=Number(i);
return g
};
v.serialize=function(g){return null==g?null:"true"==g.toString().toLowerCase()?!0:"false"==g.toString().toLowerCase()?!1:isNaN(Number(g))||5<g.length||0==g.length?g:Number(g)
}
}(jwplayer),function(d){var a="video/",m=d.foreach,h={mp4:a+"mp4",vorbis:"audio/ogg",ogg:a+"ogg",webm:a+"webm",aac:"audio/mp4",mp3:"audio/mpeg",hls:"application/vnd.apple.mpegurl"},k={mp4:h.mp4,f4v:h.mp4,m4v:h.mp4,mov:h.mp4,m4a:h.aac,f4a:h.aac,aac:h.aac,mp3:h.mp3,ogv:h.ogg,ogg:h.vorbis,oga:h.vorbis,webm:h.webm,m3u8:h.hls,hls:h.hls},a="video",a={flv:a,f4v:a,mov:a,m4a:a,m4v:a,mp4:a,aac:a,f4a:a,mp3:"sound",smil:"rtmp",m3u8:"hls",hls:"hls"},f=d.extensionmap={};
m(k,function(b,c){f[b]={html5:c}
});
m(a,function(b,c){f[b]||(f[b]={});
f[b].flash=c
});
f.types=h;
f.mimeType=function(b){var c;
m(h,function(i,g){!c&&g==b&&(c=i)
});
return c
};
f.extType=function(b){return f.mimeType(k[b])
}
}(jwplayer.utils),function(d){var a=d.loaderstatus={NEW:0,LOADING:1,ERROR:2,COMPLETE:3},f=document;
d.scriptloader=function(j){function m(){n=a.ERROR;
b.sendEvent(c.ERROR)
}function h(){n=a.COMPLETE;
b.sendEvent(c.COMPLETE)
}var n=a.NEW,c=jwplayer.events,b=new c.eventdispatcher;
d.extend(this,b);
this.load=function(){var g=d.scriptloader.loaders[j];
if(g&&(g.getStatus()==a.NEW||g.getStatus()==a.LOADING)){g.addEventListener(c.ERROR,m),g.addEventListener(c.COMPLETE,h)
}else{if(d.scriptloader.loaders[j]=this,n==a.NEW){n=a.LOADING;
var i=f.createElement("script");
i.addEventListener?(i.onload=h,i.onerror=m):i.readyState&&(i.onreadystatechange=function(){("loaded"==i.readyState||"complete"==i.readyState)&&h()
});
f.getElementsByTagName("head")[0].appendChild(i);
i.src=j
}}};
this.getStatus=function(){return n
}
};
d.scriptloader.loaders={}
}(jwplayer.utils),function(b){b.trim=function(a){return a.replace(/^\s*/,"").replace(/\s*$/,"")
};
b.pad=function(a,d,f){for(f||(f="0");
a.length<d;
){a=f+a
}return a
};
b.xmlAttribute=function(a,d){for(var f=0;
f<a.attributes.length;
f++){if(a.attributes[f].name&&a.attributes[f].name.toLowerCase()==d.toLowerCase()){return a.attributes[f].value.toString()
}}return""
};
b.extension=function(a){if(!a||"rtmp"==a.substr(0,4)){return""
}a=a.substring(a.lastIndexOf("/")+1,a.length).split("?")[0].split("#")[0];
if(-1<a.lastIndexOf(".")){return a.substr(a.lastIndexOf(".")+1,a.length).toLowerCase()
}};
b.stringToColor=function(a){a=a.replace(/(#|0x)?([0-9A-F]{3,6})$/gi,"$2");
3==a.length&&(a=a.charAt(0)+a.charAt(0)+a.charAt(1)+a.charAt(1)+a.charAt(2)+a.charAt(2));
return parseInt(a,16)
}
}(jwplayer.utils),function(d){var a="touchmove",f="touchstart";
d.touch=function(c){function h(g){g.type==f?(w=!0,m=j(l.DRAG_START,g)):g.type==a?w&&(p||(b(l.DRAG_START,g,m),p=!0),b(l.DRAG,g)):(w&&(p?b(l.DRAG_END,g):(g.cancelBubble=!0,b(l.TAP,g))),w=p=!1,m=null)
}function b(i,k,g){if(n[i]&&(k.preventManipulation&&k.preventManipulation(),k.preventDefault&&k.preventDefault(),k=g?g:j(i,k))){n[i](k)
}}function j(o,g){var i=null;
g.touches&&g.touches.length?i=g.touches[0]:g.changedTouches&&g.changedTouches.length&&(i=g.changedTouches[0]);
if(!i){return null
}var k=v.getBoundingClientRect(),i={type:o,target:v,x:i.pageX-window.pageXOffset-k.left,y:i.pageY,deltaX:0,deltaY:0};
o!=l.TAP&&m&&(i.deltaX=i.x-m.x,i.deltaY=i.y-m.y);
return i
}var v=c,w=!1,n={},m=null,p=!1,l=d.touchEvents;
document.addEventListener(a,h);
document.addEventListener("touchend",function(g){w&&p&&b(l.DRAG_END,g);
w=p=!1;
m=null
});
document.addEventListener("touchcancel",h);
c.addEventListener(f,h);
c.addEventListener("touchend",h);
this.addEventListener=function(g,i){n[g]=i
};
this.removeEventListener=function(g){delete n[g]
};
return this
}
}(jwplayer.utils),function(b){b.touchEvents={DRAG:"jwplayerDrag",DRAG_START:"jwplayerDragStart",DRAG_END:"jwplayerDragEnd",TAP:"jwplayerTap"}
}(jwplayer.utils),function(b){b.key=function(a){var m,h,j;
this.edition=function(){return j&&j.getTime()<(new Date).getTime()?"invalid":m
};
this.token=function(){return h
};
b.exists(a)||(a="");
try{a=b.tea.decrypt(a,"36QXq4W@GSBV^teR");
var f=a.split("/");
(m=f[0])?/^(free|pro|premium|ads)$/i.test(m)?(h=f[1],f[2]&&0<parseInt(f[2])&&(j=new Date,j.setTime(String(f[2])))):m="invalid":m="free"
}catch(k){m="invalid"
}}
}(jwplayer.utils),function(d){var a=d.tea={};
a.encrypt=function(c,z){if(0==c.length){return""
}var g=a.strToLongs(f.encode(c));
1>=g.length&&(g[1]=0);
for(var q=a.strToLongs(f.encode(z).slice(0,16)),x=g.length,y=g[x-1],l=g[0],m,j=Math.floor(6+52/x),b=0;
0<j--;
){b+=2654435769;
m=b>>>2&3;
for(var p=0;
p<x;
p++){l=g[(p+1)%x],y=(y>>>5^l<<2)+(l>>>3^y<<4)^(b^l)+(q[p&3^m]^y),y=g[p]+=y
}}g=a.longsToStr(g);
return h.encode(g)
};
a.decrypt=function(j,c){if(0==j.length){return""
}for(var l=a.strToLongs(h.decode(j)),w=a.strToLongs(f.encode(c).slice(0,16)),x=l.length,b=l[x-1],p=l[0],v,m=2654435769*Math.floor(6+52/x);
0!=m;
){v=m>>>2&3;
for(var g=x-1;
0<=g;
g--){b=l[0<g?g-1:x-1],b=(b>>>5^p<<2)+(p>>>3^b<<4)^(m^p)+(w[g&3^v]^b),p=l[g]-=b
}m-=2654435769
}l=a.longsToStr(l);
l=l.replace(/\0+$/,"");
return f.decode(l)
};
a.strToLongs=function(g){for(var b=Array(Math.ceil(g.length/4)),c=0;
c<b.length;
c++){b[c]=g.charCodeAt(4*c)+(g.charCodeAt(4*c+1)<<8)+(g.charCodeAt(4*c+2)<<16)+(g.charCodeAt(4*c+3)<<24)
}return b
};
a.longsToStr=function(g){for(var b=Array(g.length),c=0;
c<g.length;
c++){b[c]=String.fromCharCode(g[c]&255,g[c]>>>8&255,g[c]>>>16&255,g[c]>>>24&255)
}return b.join("")
};
var h={code:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/\x3d",encode:function(q,b){var g,x,y,z,l=[],m="",j,c,p=h.code;
c=("undefined"==typeof b?0:b)?f.encode(q):q;
j=c.length%3;
if(0<j){for(;
3>j++;
){m+="\x3d",c+="\x00"
}}for(j=0;
j<c.length;
j+=3){g=c.charCodeAt(j),x=c.charCodeAt(j+1),y=c.charCodeAt(j+2),z=g<<16|x<<8|y,g=z>>18&63,x=z>>12&63,y=z>>6&63,z&=63,l[j/3]=p.charAt(g)+p.charAt(x)+p.charAt(y)+p.charAt(z)
}l=l.join("");
return l=l.slice(0,l.length-m.length)+m
},decode:function(q,b){b="undefined"==typeof b?!1:b;
var g,x,y,z,l,m=[],j,c=h.code;
j=b?f.decode(q):q;
for(var p=0;
p<j.length;
p+=4){g=c.indexOf(j.charAt(p)),x=c.indexOf(j.charAt(p+1)),z=c.indexOf(j.charAt(p+2)),l=c.indexOf(j.charAt(p+3)),y=g<<18|x<<12|z<<6|l,g=y>>>16&255,x=y>>>8&255,y&=255,m[p/4]=String.fromCharCode(g,x,y),64==l&&(m[p/4]=String.fromCharCode(g,x)),64==z&&(m[p/4]=String.fromCharCode(g))
}z=m.join("");
return b?f.decode(z):z
}},f={encode:function(b){b=b.replace(/[\u0080-\u07ff]/g,function(c){c=c.charCodeAt(0);
return String.fromCharCode(192|c>>6,128|c&63)
});
return b=b.replace(/[\u0800-\uffff]/g,function(c){c=c.charCodeAt(0);
return String.fromCharCode(224|c>>12,128|c>>6&63,128|c&63)
})
},decode:function(b){b=b.replace(/[\u00e0-\u00ef][\u0080-\u00bf][\u0080-\u00bf]/g,function(c){c=(c.charCodeAt(0)&15)<<12|(c.charCodeAt(1)&63)<<6|c.charCodeAt(2)&63;
return String.fromCharCode(c)
});
return b=b.replace(/[\u00c0-\u00df][\u0080-\u00bf]/g,function(c){c=(c.charCodeAt(0)&31)<<6|c.charCodeAt(1)&63;
return String.fromCharCode(c)
})
}}
}(jwplayer.utils),function(b){b.events={COMPLETE:"COMPLETE",ERROR:"ERROR",API_READY:"jwplayerAPIReady",JWPLAYER_READY:"jwplayerReady",JWPLAYER_FULLSCREEN:"jwplayerFullscreen",JWPLAYER_RESIZE:"jwplayerResize",JWPLAYER_ERROR:"jwplayerError",JWPLAYER_SETUP_ERROR:"jwplayerSetupError",JWPLAYER_MEDIA_BEFOREPLAY:"jwplayerMediaBeforePlay",JWPLAYER_MEDIA_BEFORECOMPLETE:"jwplayerMediaBeforeComplete",JWPLAYER_COMPONENT_SHOW:"jwplayerComponentShow",JWPLAYER_COMPONENT_HIDE:"jwplayerComponentHide",JWPLAYER_MEDIA_BUFFER:"jwplayerMediaBuffer",JWPLAYER_MEDIA_BUFFER_FULL:"jwplayerMediaBufferFull",JWPLAYER_MEDIA_ERROR:"jwplayerMediaError",JWPLAYER_MEDIA_LOADED:"jwplayerMediaLoaded",JWPLAYER_MEDIA_COMPLETE:"jwplayerMediaComplete",JWPLAYER_MEDIA_SEEK:"jwplayerMediaSeek",JWPLAYER_MEDIA_TIME:"jwplayerMediaTime",JWPLAYER_MEDIA_VOLUME:"jwplayerMediaVolume",JWPLAYER_MEDIA_META:"jwplayerMediaMeta",JWPLAYER_MEDIA_MUTE:"jwplayerMediaMute",JWPLAYER_MEDIA_LEVELS:"jwplayerMediaLevels",JWPLAYER_MEDIA_LEVEL_CHANGED:"jwplayerMediaLevelChanged",JWPLAYER_CAPTIONS_CHANGED:"jwplayerCaptionsChanged",JWPLAYER_CAPTIONS_LIST:"jwplayerCaptionsList",JWPLAYER_PLAYER_STATE:"jwplayerPlayerState",state:{BUFFERING:"BUFFERING",IDLE:"IDLE",PAUSED:"PAUSED",PLAYING:"PLAYING"},JWPLAYER_PLAYLIST_LOADED:"jwplayerPlaylistLoaded",JWPLAYER_PLAYLIST_ITEM:"jwplayerPlaylistItem",JWPLAYER_PLAYLIST_COMPLETE:"jwplayerPlaylistComplete",JWPLAYER_DISPLAY_CLICK:"jwplayerViewClick",JWPLAYER_CONTROLS:"jwplayerViewControls",JWPLAYER_USER_ACTION:"jwplayerUserAction",JWPLAYER_INSTREAM_CLICK:"jwplayerInstreamClicked",JWPLAYER_INSTREAM_DESTROYED:"jwplayerInstreamDestroyed",JWPLAYER_AD_TIME:"jwplayerAdTime",JWPLAYER_AD_ERROR:"jwplayerAdError",JWPLAYER_AD_CLICK:"jwplayerAdClicked",JWPLAYER_AD_COMPLETE:"jwplayerAdComplete",JWPLAYER_AD_IMPRESSION:"jwplayerAdImpression",JWPLAYER_AD_COMPANIONS:"jwplayerAdCompanions"}
}(jwplayer),function(d){var a=jwplayer.utils;
d.eventdispatcher=function(c,h){var b,f;
this.resetEventListeners=function(){b={};
f=[]
};
this.resetEventListeners();
this.addEventListener=function(i,m,g){try{a.exists(b[i])||(b[i]=[]),"string"==a.typeOf(m)&&(m=(new Function("return "+m))()),b[i].push({listener:m,count:g})
}catch(j){a.log("error",j)
}return !1
};
this.removeEventListener=function(i,m){if(b[i]){try{for(var g=0;
g<b[i].length;
g++){if(b[i][g].listener.toString()==m.toString()){b[i].splice(g,1);
break
}}}catch(j){a.log("error",j)
}return !1
}};
this.addGlobalListener=function(i,j){try{"string"==a.typeOf(i)&&(i=(new Function("return "+i))()),f.push({listener:i,count:j})
}catch(g){a.log("error",g)
}return !1
};
this.removeGlobalListener=function(i){if(i){try{for(var j=0;
j<f.length;
j++){if(f[j].listener.toString()==i.toString()){f.splice(j,1);
break
}}}catch(g){a.log("error",g)
}return !1
}};
this.sendEvent=function(j,l){a.exists(l)||(l={});
a.extend(l,{id:c,version:jwplayer.version,type:j});
h&&a.log(j,l);
if("undefined"!=a.typeOf(b[j])){for(var g=0;
g<b[j].length;
g++){try{b[j][g].listener(l)
}catch(i){a.log("There was an error while handling a listener: "+i.toString(),b[j][g].listener)
}b[j][g]&&(1===b[j][g].count?delete b[j][g]:0<b[j][g].count&&(b[j][g].count-=1))
}}for(g=0;
g<f.length;
g++){try{f[g].listener(l)
}catch(m){a.log("There was an error while handling a listener: "+m.toString(),f[g].listener)
}f[g]&&(1===f[g].count?delete f[g]:0<f[g].count&&(f[g].count-=1))
}}
}
}(jwplayer.events),function(d){var a={},f={};
d.plugins=function(){};
d.plugins.loadPlugins=function(c,b){f[c]=new d.plugins.pluginloader(new d.plugins.model(a),b);
return f[c]
};
d.plugins.registerPlugin=function(h,j,c,l){var b=d.utils.getPluginName(h);
a[b]||(a[b]=new d.plugins.plugin(h));
a[b].registerPlugin(h,j,c,l)
}
}(jwplayer),function(b){b.plugins.model=function(a){this.addPlugin=function(g){var f=b.utils.getPluginName(g);
a[f]||(a[f]=new b.plugins.plugin(g));
return a[f]
};
this.getPlugins=function(){return a
}
}
}(jwplayer),function(d){var a=jwplayer.utils,f=jwplayer.events;
d.pluginmodes={FLASH:0,JAVASCRIPT:1,HYBRID:2};
d.plugin=function(c){function h(){switch(a.getPluginPathType(c)){case a.pluginPathType.ABSOLUTE:return c;
case a.pluginPathType.RELATIVE:return a.getAbsolutePath(c,window.location.href)
}}function b(){p=setTimeout(function(){v=a.loaderstatus.COMPLETE;
l.sendEvent(f.COMPLETE)
},1000)
}function j(){v=a.loaderstatus.ERROR;
l.sendEvent(f.ERROR)
}var v=a.loaderstatus.NEW,w,n,m,p,l=new f.eventdispatcher;
a.extend(this,l);
this.load=function(){if(v==a.loaderstatus.NEW){if(0<c.lastIndexOf(".swf")){w=c,v=a.loaderstatus.COMPLETE,l.sendEvent(f.COMPLETE)
}else{if(a.getPluginPathType(c)==a.pluginPathType.CDN){v=a.loaderstatus.COMPLETE,l.sendEvent(f.COMPLETE)
}else{v=a.loaderstatus.LOADING;
var g=new a.scriptloader(h());
g.addEventListener(f.COMPLETE,b);
g.addEventListener(f.ERROR,j);
g.load()
}}}};
this.registerPlugin=function(g,i,k,o){p&&(clearTimeout(p),p=void 0);
m=i;
k&&o?(w=o,n=k):"string"==typeof k?w=k:"function"==typeof k?n=k:!k&&!o&&(w=g);
v=a.loaderstatus.COMPLETE;
l.sendEvent(f.COMPLETE)
};
this.getStatus=function(){return v
};
this.getPluginName=function(){return a.getPluginName(c)
};
this.getFlashPath=function(){if(w){switch(a.getPluginPathType(w)){case a.pluginPathType.ABSOLUTE:return w;
case a.pluginPathType.RELATIVE:return 0<c.lastIndexOf(".swf")?a.getAbsolutePath(w,window.location.href):a.getAbsolutePath(w,h())
}}return null
};
this.getJS=function(){return n
};
this.getTarget=function(){return m
};
this.getPluginmode=function(){if("undefined"!=typeof w&&"undefined"!=typeof n){return d.pluginmodes.HYBRID
}if("undefined"!=typeof w){return d.pluginmodes.FLASH
}if("undefined"!=typeof n){return d.pluginmodes.JAVASCRIPT
}};
this.getNewInstance=function(i,k,g){return new n(i,k,g)
};
this.getURL=function(){return c
}
}
}(jwplayer.plugins),function(d){var a=d.utils,h=d.events,f=a.foreach;
d.plugins.pluginloader=function(b,x){function c(){j?y.sendEvent(h.ERROR,{message:m}):l||(l=!0,q=a.loaderstatus.COMPLETE,y.sendEvent(h.COMPLETE))
}function p(){g||c();
if(!l&&!j){var k=0,i=b.getPlugins();
a.foreach(g,function(t){t=a.getPluginName(t);
var o=i[t];
t=o.getJS();
var r=o.getTarget(),o=o.getStatus();
if(o==a.loaderstatus.LOADING||o==a.loaderstatus.NEW){k++
}else{if(t&&(!r||parseFloat(r)>parseFloat(d.version))){j=!0,m="Incompatible player version",c()
}}});
0==k&&c()
}}var q=a.loaderstatus.NEW,l=!1,j=!1,m,g=x,y=new h.eventdispatcher;
a.extend(this,y);
this.setupPlugins=function(r,v,u){var k={length:0,plugins:{}},o=0,t={},i=b.getPlugins();
f(v.plugins,function(K,L){var M=a.getPluginName(K),N=i[M],w=N.getFlashPath(),D=N.getJS(),J=N.getURL();
w&&(k.plugins[w]=a.extend({},L),k.plugins[w].pluginmode=N.getPluginmode(),k.length++);
try{if(D&&v.plugins&&v.plugins[J]){var A=document.createElement("div");
A.id=r.id+"_"+M;
A.style.position="absolute";
A.style.top=0;
A.style.zIndex=o+10;
t[M]=N.getNewInstance(r,a.extend({},v.plugins[J]),A);
o++;
r.onReady(u(t[M],A,!0));
r.onResize(u(t[M],A))
}}catch(I){a.log("ERROR: Failed to load "+M+".")
}});
r.plugins=t;
return k
};
this.load=function(){if(!(a.exists(x)&&"object"!=a.typeOf(x))){q=a.loaderstatus.LOADING;
f(x,function(k){a.exists(k)&&(k=b.addPlugin(k),k.addEventListener(h.COMPLETE,p),k.addEventListener(h.ERROR,n))
});
var i=b.getPlugins();
f(i,function(k,o){o.load()
})
}p()
};
var n=this.pluginFailed=function(){j||(j=!0,m="File not found",c())
};
this.getStatus=function(){return q
}
}
}(jwplayer),function(){jwplayer.parsers={localName:function(b){return b?b.localName?b.localName:b.baseName?b.baseName:"":""
},textContent:function(b){return b?b.textContent?b.textContent:b.text?b.text:"":""
},getChildNode:function(d,a){return d.childNodes[a]
},numChildren:function(b){return b.childNodes?b.childNodes.length:0
}}
}(jwplayer),function(d){var a=d.parsers;
(a.jwparser=function(){}).parseEntry=function(q,f){for(var h=[],b=[],j=d.utils.xmlAttribute,c=0;
c<q.childNodes.length;
c++){var k=q.childNodes[c];
if("jwplayer"==k.prefix){var n=a.localName(k);
"source"==n?(delete f.sources,h.push({file:j(k,"file"),"default":j(k,"default"),label:j(k,"label"),type:j(k,"type")})):"track"==n?(delete f.tracks,b.push({file:j(k,"file"),"default":j(k,"default"),kind:j(k,"kind"),label:j(k,"label")})):(f[n]=d.utils.serialize(a.textContent(k)),"file"==n&&f.sources&&delete f.sources)
}f.file||(f.file=f.link)
}if(h.length){f.sources=[];
for(c=0;
c<h.length;
c++){0<h[c].file.length&&(h[c]["default"]="true"==h[c]["default"]?!0:!1,h[c].label.length||delete h[c].label,f.sources.push(h[c]))
}}if(b.length){f.tracks=[];
for(c=0;
c<b.length;
c++){0<b[c].file.length&&(b[c]["default"]="true"==b[c]["default"]?!0:!1,b[c].kind=!b[c].kind.length?"captions":b[c].kind,b[c].label.length||delete b[c].label,f.tracks.push(b[c]))
}}return f
}
}(jwplayer),function(o){var d=jwplayer.utils,k=d.xmlAttribute,f=o.localName,h=o.textContent,a=o.numChildren,j=o.mediaparser=function(){};
j.parseGroup=function(n,l){var p,b,c=[];
for(b=0;
b<a(n);
b++){if(p=n.childNodes[b],"media"==p.prefix&&f(p)){switch(f(p).toLowerCase()){case"content":k(p,"duration")&&(l.duration=d.seconds(k(p,"duration")));
0<a(p)&&(l=j.parseGroup(p,l));
k(p,"url")&&(l.sources||(l.sources=[]),l.sources.push({file:k(p,"url"),type:k(p,"type"),width:k(p,"width"),label:k(p,"label")}));
break;
case"title":l.title=h(p);
break;
case"description":l.description=h(p);
break;
case"guid":l.mediaid=h(p);
break;
case"thumbnail":l.image||(l.image=k(p,"url"));
break;
case"group":j.parseGroup(p,l);
break;
case"subtitle":var m={};
m.file=k(p,"url");
m.kind="captions";
if(0<k(p,"lang").length){var i=m;
p=k(p,"lang");
var g={zh:"Chinese",nl:"Dutch",en:"English",fr:"French",de:"German",it:"Italian",ja:"Japanese",pt:"Portuguese",ru:"Russian",es:"Spanish"};
p=g[p]?g[p]:p;
i.label=p
}c.push(m)
}}}l.hasOwnProperty("tracks")||(l.tracks=[]);
for(b=0;
b<c.length;
b++){l.tracks.push(c[b])
}return l
}
}(jwplayer.parsers),function(o){function d(l){for(var i={},b=0;
b<l.childNodes.length;
b++){var g=l.childNodes[b],c=j(g);
if(c){switch(c.toLowerCase()){case"enclosure":i.file=k.xmlAttribute(g,"url");
break;
case"title":i.title=f(g);
break;
case"guid":i.mediaid=f(g);
break;
case"pubdate":i.date=f(g);
break;
case"description":i.description=f(g);
break;
case"link":i.link=f(g);
break;
case"category":i.tags=i.tags?i.tags+f(g):f(g)
}}}i=o.mediaparser.parseGroup(l,i);
i=o.jwparser.parseEntry(l,i);
return new jwplayer.playlist.item(i)
}var k=jwplayer.utils,f=o.textContent,h=o.getChildNode,a=o.numChildren,j=o.localName;
o.rssparser={};
o.rssparser.parse=function(b){for(var l=[],c=0;
c<a(b);
c++){var m=h(b,c);
if("channel"==j(m).toLowerCase()){for(var g=0;
g<a(m);
g++){var i=h(m,g);
"item"==j(i).toLowerCase()&&l.push(d(i))
}}}return l
}
}(jwplayer.parsers),function(b){b.playlist=function(a){var g=[];
if("array"==b.utils.typeOf(a)){for(var f=0;
f<a.length;
f++){g.push(new b.playlist.item(a[f]))
}}else{g.push(new b.playlist.item(a))
}return g
}
}(jwplayer),function(d){var a=d.item=function(c){var f=jwplayer.utils,h=f.extend({},a.defaults,c);
h.tracks=c&&f.exists(c.tracks)?c.tracks:[];
0==h.sources.length&&(h.sources=[new d.source(h)]);
for(var b=0;
b<h.sources.length;
b++){var j=h.sources[b]["default"];
h.sources[b]["default"]=j?"true"==j.toString():!1;
h.sources[b]=new d.source(h.sources[b])
}if(h.captions&&!f.exists(c.tracks)){for(c=0;
c<h.captions.length;
c++){h.tracks.push(h.captions[c])
}delete h.captions
}for(b=0;
b<h.tracks.length;
b++){h.tracks[b]=new d.track(h.tracks[b])
}return h
};
a.defaults={description:"",image:"",mediaid:"",title:"",sources:[],tracks:[]}
}(jwplayer.playlist),function(d){var a=jwplayer,j=a.utils,f=a.events,h=a.parsers;
d.loader=function(){function g(q){try{var t=q.responseXML.childNodes;
q="";
for(var k=0;
k<t.length&&!(q=t[k],8!=q.nodeType);
k++){}"xml"==h.localName(q)&&(q=q.nextSibling);
if("rss"!=h.localName(q)){i("Not a valid RSS feed")
}else{var l=new d(h.rssparser.parse(q));
b.sendEvent(f.JWPLAYER_PLAYLIST_LOADED,{playlist:l})
}}catch(r){i()
}}function c(k){i(k.match(/invalid/i)?"Not a valid RSS feed":"")
}function i(k){b.sendEvent(f.JWPLAYER_ERROR,{message:k?k:"Error loading file"})
}var b=new f.eventdispatcher;
j.extend(this,b);
this.load=function(k){j.ajax(k,g,c)
}
}
}(jwplayer.playlist),function(d){var a=jwplayer.utils,f={file:void 0,label:void 0,type:void 0,"default":void 0};
d.source=function(b){var c=a.extend({},f);
a.foreach(f,function(g){a.exists(b[g])&&(c[g]=b[g],delete b[g])
});
c.type&&0<c.type.indexOf("/")&&(c.type=a.extensionmap.mimeType(c.type));
"m3u8"==c.type&&(c.type="hls");
"smil"==c.type&&(c.type="rtmp");
return c
}
}(jwplayer.playlist),function(d){var a=jwplayer.utils,f={file:void 0,label:void 0,kind:"captions","default":!1};
d.track=function(c){var b=a.extend({},f);
c||(c={});
a.foreach(f,function(g){a.exists(c[g])&&(b[g]=c[g],delete c[g])
});
return b
}
}(jwplayer.playlist),function(o){var d=o.utils,k=o.events,f=!0,h=!1,a=document,j=o.embed=function(b){function c(C,A){d.foreach(A,function(E,D){"function"==typeof C[E]&&C[E].call(C,D)
})
}function m(){if(r.sitecatalyst){try{null!=s&&s.hasOwnProperty("Media")||i()
}catch(A){i();
return
}}if("array"==d.typeOf(r.playlist)&&2>r.playlist.length&&(0==r.playlist.length||!r.playlist[0].sources||0==r.playlist[0].sources.length)){n()
}else{if(!B){if("string"==d.typeOf(r.playlist)){var C=new o.playlist.loader;
C.addEventListener(k.JWPLAYER_PLAYLIST_LOADED,function(G){r.playlist=G.playlist;
B=h;
m()
});
C.addEventListener(k.JWPLAYER_ERROR,function(G){B=h;
n(G)
});
B=f;
C.load(r.playlist)
}else{if(z.getStatus()==d.loaderstatus.COMPLETE){for(C=0;
C<r.modes.length;
C++){if(r.modes[C].type&&j[r.modes[C].type]){var D=d.extend({},r),E=new j[r.modes[C].type](u,r.modes[C],D,z,b);
if(E.supportsConfig()){return E.addEventListener(k.ERROR,l),E.embed(),c(b,D.events),b
}}}if(r.fallback){var F="No suitable players found and fallback enabled";
t=setTimeout(function(){p(F,f)
},10);
d.log(F);
new j.download(u,r,n)
}else{F="No suitable players found and fallback disabled",p(F,h),d.log(F),u.parentNode.replaceChild(w,u)
}}}}}}function l(A){g(u,q+A.message)
}function n(A){A&&A.message?g(u,"Error loading playlist: "+A.message):g(u,q+"No playable sources found")
}function i(){g(u,"Adobe SiteCatalyst Error: Could not find Media Module")
}function g(E,A){if(r.fallback){var D=E.style;
D.backgroundColor="#000";
D.color="#FFF";
D.width=d.styleDimension(r.width);
D.height=d.styleDimension(r.height);
D.display="table";
D.opacity=1;
var D=document.createElement("p"),C=D.style;
C.verticalAlign="middle";
C.textAlign="center";
C.display="table-cell";
C.font="15px/20px Arial, Helvetica, sans-serif";
D.innerHTML=A.replace(":",":\x3cbr\x3e");
E.innerHTML="";
E.appendChild(D);
p(A,f)
}else{p(A,h)
}}function p(C,A){t&&(clearTimeout(t),t=null);
b.dispatchEvent(k.JWPLAYER_SETUP_ERROR,{message:C,fallback:A})
}var r=new j.config(b.config),u,v,w,x=r.width,y=r.height,q="Error loading player: ",z=o.plugins.loadPlugins(b.id,r.plugins),B=h,t=null;
r.fallbackDiv&&(w=r.fallbackDiv,delete r.fallbackDiv);
r.id=b.id;
v=a.getElementById(b.id);
r.aspectratio?b.config.aspectratio=r.aspectratio:delete b.config.aspectratio;
u=a.createElement("div");
u.id=v.id;
u.style.width=0<x.toString().indexOf("%")?x:x+"px";
u.style.height=0<y.toString().indexOf("%")?y:y+"px";
v.parentNode.replaceChild(u,v);
o.embed.errorScreen=g;
z.addEventListener(k.COMPLETE,m);
z.addEventListener(k.ERROR,function(A){g(u,"Could not load plugins: "+A.message)
});
z.load();
return b
}
}(jwplayer),function(d){function a(c){if(c.playlist){for(var b=0;
b<c.playlist.length;
b++){c.playlist[b]=new h(c.playlist[b])
}}else{var g={};
f.foreach(h.defaults,function(i){j(c,g,i)
});
g.sources||(c.levels?(g.sources=c.levels,delete c.levels):(b={},j(c,b,"file"),j(c,b,"type"),g.sources=b.file?[b]:[]));
c.playlist=[new h(g)]
}}function j(c,b,g){f.exists(c[g])&&(b[g]=c[g],delete c[g])
}var f=d.utils,h=d.playlist.item;
(d.embed.config=function(g){var i={fallback:!0,height:270,primary:"html5",width:480,base:g.base?g.base:f.getScriptPath("jwplayer.js"),aspectratio:""};
g=f.extend(i,d.defaults,g);
var i={type:"html5",src:"https://consumer.huawei.com/en/ucmf/groups/public/documents/webasset/jwplayer_cej.html5.js"},b={type:"flash",src:g.base+"jwplayer.flash.swf"};
g.modes="flash"==g.primary?[b,i]:[i,b];
g.listbar&&(g.playlistsize=g.listbar.size,g.playlistposition=g.listbar.position,g.playlistlayout=g.listbar.layout);
g.flashplayer&&(b.src=g.flashplayer);
g.html5player&&(i.src=g.html5player);
a(g);
b=g.aspectratio;
if("string"!=typeof b||!f.exists(b)){i=0
}else{var c=b.indexOf(":");
-1==c?i=0:(i=parseFloat(b.substr(0,c)),b=parseFloat(b.substr(c+1)),i=0>=i||0>=b?0:100*(b/i)+"%")
}-1==g.width.toString().indexOf("%")?delete g.aspectratio:i?g.aspectratio=i:delete g.aspectratio;
return g
}).addConfig=function(b,c){a(c);
return f.extend(b,c)
}
}(jwplayer),function(d){var a=d.utils,f=document;
d.embed.download=function(g,q,j){function t(w,i){for(var o=f.querySelectorAll(w),k=0;
k<o.length;
k++){a.foreach(i,function(x,y){o[k].style[x]=y
})
}}function b(k,o,i){k=f.createElement(k);
o&&(k.className="jwdownload"+o);
i&&i.appendChild(k);
return k
}var c=a.extend({},q),l=c.width?c.width:480,h=c.height?c.height:320,m;
q=q.logo?q.logo:{prefix:a.repo(),file:"logo.png",margin:10};
var u,p,n,c=c.playlist,r,v=["mp4","aac","mp3"];
if(c&&c.length){r=c[0];
m=r.sources;
for(c=0;
c<m.length;
c++){var H=m[c],I=H.type?H.type:a.extensionmap.extType(a.extension(H.file));
H.file&&a.foreach(v,function(i){I==v[i]?(u=H.file,p=r.image):a.isYouTube(H.file)&&(n=H.file)
})
}u?(m=u,j=p,g&&(c=b("a","display",g),b("div","icon",c),b("div","logo",c),m&&c.setAttribute("href",a.getAbsolutePath(m))),c="#"+g.id+" .jwdownload",g.style.width="",g.style.height="",t(c+"display",{width:a.styleDimension(Math.max(320,l)),height:a.styleDimension(Math.max(180,h)),background:"black center no-repeat "+(j?"url("+j+")":""),backgroundSize:"contain",position:"relative",border:"none",display:"block"}),t(c+"display div",{position:"absolute",width:"100%",height:"100%"}),t(c+"logo",{top:q.margin+"px",right:q.margin+"px",background:"top right no-repeat url("+q.prefix+q.file+")"}),t(c+"icon",{background:"center no-repeat url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8CAYAAAA6/NlyAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAgNJREFUeNrs28lqwkAYB/CZqNVDDj2r6FN41QeIy8Fe+gj6BL275Q08u9FbT8ZdwVfotSBYEPUkxFOoks4EKiJdaDuTjMn3wWBO0V/+sySR8SNSqVRKIR8qaXHkzlqS9jCfzzWcTCYp9hF5o+59sVjsiRzcegSckFzcjT+ruN80TeSlAjCAAXzdJSGPFXRpAAMYwACGZQkSdhG4WCzehMNhqV6vG6vVSrirKVEw66YoSqDb7cqlUilE8JjHd/y1MQefVzqdDmiaJpfLZWHgXMHn8F6vJ1cqlVAkEsGuAn83J4gAd2RZymQygX6/L1erVQt+9ZPWb+CDwcCC2zXGJaewl/DhcHhK3DVj+KfKZrMWvFarcYNLomAv4aPRSFZVlTlcSPA5fDweW/BoNIqFnKV53JvncjkLns/n/cLdS+92O7RYLLgsKfv9/t8XlDn4eDyiw+HA9Jyz2eyt0+kY2+3WFC5hluej0Ha7zQQq9PPwdDq1Et1sNsx/nFBgCqWJ8oAK1aUptNVqcYWewE4nahfU0YQnk4ntUEfGMIU2m01HoLaCKbTRaDgKtaVLk9tBYaBcE/6Artdr4RZ5TB6/dC+9iIe/WgAMYADDpAUJAxjAAAYwgGFZgoS/AtNNTF7Z2bL0BYPBV3Jw5xFwwWcYxgtBP5OkE8i9G7aWGOOCruvauwADALMLMEbKf4SdAAAAAElFTkSuQmCC)"})):n?(q=n,g=b("embed","",g),g.src="http://www.youtube.com/v/"+a.youTubeID(q),g.type="application/x-shockwave-flash",g.width=l,g.height=h):j()
}}
}(jwplayer),function(d){var a=d.utils,j=d.events,f={};
(d.embed.flash=function(w,c,p,q,l){function i(o,r,t){var k=document.createElement("param");
k.setAttribute("name",r);
k.setAttribute("value",t);
o.appendChild(k)
}function m(o,r,k){return function(){try{k&&document.getElementById(l.id+"_wrapper").appendChild(r);
var u=document.getElementById(l.id).getPluginConfig("display");
"function"==typeof o.resize&&o.resize(u.width,u.height);
r.style.left=u.x;
r.style.top=u.h
}catch(t){}}
}function g(r){if(!r){return{}
}var k={},o=[];
a.foreach(r,function(v,t){var u=a.getPluginName(v);
o.push(v);
a.foreach(t,function(y,z){k[u+"."+y]=z
})
});
k.plugins=o.join(",");
return k
}var b=new d.events.eventdispatcher,n=a.flashVersion();
a.extend(this,b);
this.embed=function(){p.id=l.id;
if(10>n){return b.sendEvent(j.ERROR,{message:"Flash version must be 10.0 or greater"}),!1
}var t,u,k=l.config.listbar,o=a.extend({},p);
if(w.id+"_wrapper"==w.parentNode.id){t=document.getElementById(w.id+"_wrapper")
}else{t=document.createElement("div");
u=document.createElement("div");
u.style.display="none";
u.id=w.id+"_aspect";
t.id=w.id+"_wrapper";
t.style.position="relative";
t.style.display="block";
t.style.width=a.styleDimension(o.width);
t.style.height=a.styleDimension(o.height);
if(l.config.aspectratio){var r=parseFloat(l.config.aspectratio);
u.style.display="block";
u.style.marginTop=l.config.aspectratio;
t.style.height="auto";
t.style.display="inline-block";
k&&("bottom"==k.position?u.style.paddingBottom=k.size+"px":"right"==k.position&&(u.style.marginBottom=-1*k.size*(r/100)+"px"))
}w.parentNode.replaceChild(t,w);
t.appendChild(w);
t.appendChild(u)
}t=q.setupPlugins(l,o,m);
0<t.length?a.extend(o,g(t.plugins)):delete o.plugins;
"undefined"!=typeof o["dock.position"]&&"false"==o["dock.position"].toString().toLowerCase()&&(o.dock=o["dock.position"],delete o["dock.position"]);
t=o.wmode?o.wmode:o.height&&40>=o.height?"transparent":"opaque";
u="height width modes events primary base fallback volume".split(" ");
for(k=0;
k<u.length;
k++){delete o[u[k]]
}u=a.getCookies();
a.foreach(u,function(v,x){"undefined"==typeof o[v]&&(o[v]=x)
});
u=window.location.href.split("/");
u.splice(u.length-1,1);
u=u.join("/");
o.base=u+"/";
f[w.id]=o;
a.isIE()?(u='\x3cobject classid\x3d"clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" " width\x3d"100%" height\x3d"100%"id\x3d"'+w.id+'" name\x3d"'+w.id+'" tabindex\x3d0""\x3e',u+='\x3cparam name\x3d"movie" value\x3d"'+c.src+'"\x3e',u+='\x3cparam name\x3d"allowfullscreen" value\x3d"true"\x3e\x3cparam name\x3d"allowscriptaccess" value\x3d"always"\x3e',u+='\x3cparam name\x3d"seamlesstabbing" value\x3d"true"\x3e',u+='\x3cparam name\x3d"wmode" value\x3d"'+t+'"\x3e',u+='\x3cparam name\x3d"bgcolor" value\x3d"#000000"\x3e',u+="\x3c/object\x3e",w.outerHTML=u,t=document.getElementById(w.id)):(u=document.createElement("object"),u.setAttribute("type","application/x-shockwave-flash"),u.setAttribute("data",c.src),u.setAttribute("width","100%"),u.setAttribute("height","100%"),u.setAttribute("bgcolor","#000000"),u.setAttribute("id",w.id),u.setAttribute("name",w.id),u.setAttribute("tabindex",0),i(u,"allowfullscreen","true"),i(u,"allowscriptaccess","always"),i(u,"seamlesstabbing","true"),i(u,"wmode",t),w.parentNode.replaceChild(u,w),t=u);
l.config.aspectratio&&(t.style.position="absolute");
l.container=t;
l.setPlayer(t,"flash")
};
this.supportsConfig=function(){if(n){if(p){if("string"==a.typeOf(p.playlist)){return !0
}try{var k=p.playlist[0].sources;
if("undefined"==typeof k){return !0
}for(var o=0;
o<k.length;
o++){if(k[o].file&&h(k[o].file,k[o].type)){return !0
}}}catch(r){}}else{return !0
}}return !1
}
}).getVars=function(b){return f[b]
};
var h=d.embed.flashCanPlay=function(c,g){if(a.isYouTube(c)||a.isRtmp(c,g)||"hls"==g){return !0
}var b=a.extensionmap[g?g:a.extension(c)];
return !b?!1:!!b.flash
}
}(jwplayer),function(d){var a=d.utils,h=a.extensionmap,f=d.events;
d.embed.html5=function(g,c,j,u,b){function n(k,o,i){return function(){try{var r=document.querySelector("#"+g.id+" .jwmain");
i&&r.appendChild(o);
"function"==typeof k.resize&&(k.resize(r.clientWidth,r.clientHeight),setTimeout(function(){k.resize(r.clientWidth,r.clientHeight)
},400));
o.left=r.style.left;
o.top=r.style.top
}catch(q){}}
}function m(i){p.sendEvent(i.type,{message:"HTML5 player not found"})
}var p=this,l=new f.eventdispatcher;
a.extend(p,l);
p.embed=function(){if(d.html5){u.setupPlugins(b,j,n);
g.innerHTML="";
var i=d.utils.extend({},j);
delete i.volume;
i=new d.html5.player(i);
b.container=document.getElementById(b.id);
b.setPlayer(i,"html5")
}else{i=new a.scriptloader(c.src),i.addEventListener(f.ERROR,m),i.addEventListener(f.COMPLETE,p.embed),i.load()
}};
p.supportsConfig=function(){if(d.vid.canPlayType){try{if("string"==a.typeOf(j.playlist)){return !0
}for(var H=j.playlist[0].sources,i=0;
i<H.length;
i++){var o;
var q=H[i].file,t=H[i].type;
if(null!==navigator.userAgent.match(/BlackBerry/i)||a.isAndroid()&&("m3u"==a.extension(q)||"m3u8"==a.extension(q))||a.isRtmp(q,t)){o=!1
}else{var y=h[t?t:a.extension(q)],z;
if(!y||y.flash&&!y.html5){z=!1
}else{var G=y.html5,r=d.vid;
if(G){try{z=r.canPlayType(G)?!0:!1
}catch(I){z=!1
}}else{z=!0
}}o=z
}if(o){return !0
}}}catch(k){}}return !1
}
}
}(jwplayer),function(d){var a=d.embed,h=d.utils,f=h.extend(function(r){var q=h.repo(),A=h.extend({},d.defaults),m=h.extend({},A,r.config),p=r.config,g=m.plugins,c=m.analytics,j=q+"jwpsrv.js",b=q+"sharing.js",z=q+"related.js",l=q+"gapro.js",A=d.key?d.key:A.key,n=(new d.utils.key(A)).edition(),g=g?g:{};
"ads"==n&&m.advertising&&(m.advertising.client.match(".js$|.swf$")?g[m.advertising.client]=m.advertising:g[q+m.advertising.client+".js"]=m.advertising);
delete p.advertising;
p.key=A;
m.analytics&&(m.analytics.client&&m.analytics.client.match(".js$|.swf$"))&&(j=m.analytics.client);
delete p.analytics;
if("free"==n||!c||!1!==c.enabled){g[j]=c?c:{}
}delete g.sharing;
delete g.related;
switch(n){case"premium":case"ads":m.related&&(m.related.client&&m.related.client.match(".js$|.swf$")&&(z=m.related.client),g[z]=m.related),m.ga&&(m.ga.client&&m.ga.client.match(".js$|.swf$")&&(l=m.ga.client),g[l]=m.ga),p.sitecatalyst&&new d.embed.sitecatalyst(r);
case"pro":m.sharing&&(m.sharing.client&&m.sharing.client.match(".js$|.swf$")&&(b=m.sharing.client),g[b]=m.sharing),m.skin&&(p.skin=m.skin.replace(/^(beelden|bekle|five|glow|modieus|roundster|stormtrooper|vapor)$/i,h.repo()+"skins/$1.xml"))
}p.plugins=g;
return new a(r)
},a);
d.embed=f
}(jwplayer),function(d){var a=jwplayer.utils;
d.sitecatalyst=function(g){function m(i){c.debug&&a.log(i)
}function q(i){i=i.split("/");
i=i[i.length-1];
i=i.split("?");
return i[0]
}function l(){if(!p){p=!0;
var i=b.getPosition();
m("stop: "+E+" : "+i);
s.Media.stop(E,i)
}}function r(){j||(l(),j=!0,m("close: "+E),s.Media.close(E),n=!0,D=0)
}var b=g,c=a.extend({},b.config.sitecatalyst),f={onPlay:function(){if(!n){var i=b.getPosition();
p=!1;
m("play: "+E+" : "+i);
s.Media.play(E,i)
}},onPause:l,onBuffer:l,onIdle:r,onPlaylistItem:function(i){try{n=!0;
r();
D=0;
var k;
if(c.mediaName){k=c.mediaName
}else{var t=b.getPlaylistItem(i.index);
k=t.title?t.title:t.file?q(t.file):t.sources&&t.sources.length?q(t.sources[0].file):""
}E=k;
h=c.playerName?c.playerName:b.id
}catch(o){a.log(o)
}},onTime:function(){if(n){var k=b.getDuration();
if(-1==k){return
}j=p=n=!1;
m("open: "+E+" : "+k+" : "+h);
s.Media.open(E,k,h);
m("play: "+E+" : 0");
s.Media.play(E,0)
}k=b.getPosition();
if(3<=Math.abs(k-D)){var i=D;
m("seek: "+i+" to "+k);
m("stop: "+E+" : "+i);
s.Media.stop(E,i);
m("play: "+E+" : "+k);
s.Media.play(E,k)
}D=k
},onComplete:r},E,h,D,p=!0,j=!0,n;
a.foreach(f,function(i){b[i](f[i])
})
}
}(jwplayer.embed),function(o){var d=[],k=o.utils,f=o.events,h=f.state,a=document,j=o.api=function(x){function b(A,B){return function(C){return B(A,C)
}
}function m(A,B){r[A]||(r[A]=[],n(f.JWPLAYER_PLAYER_STATE,function(C){var D=C.newstate;
C=C.oldstate;
if(D==A){var E=r[D];
if(E){for(var F=0;
F<E.length;
F++){"function"==typeof E[F]&&E[F].call(this,{oldstate:C,newstate:D})
}}}}));
r[A].push(B);
return i
}function l(B,C){try{B.jwAddEventListener(C,'function(dat) { jwplayer("'+i.id+'").dispatchEvent("'+C+'", dat); }')
}catch(A){k.log("Could not add internal listener")
}}function n(A,B){q[A]||(q[A]=[],t&&u&&l(t,A));
q[A].push(B);
return i
}function g(){if(u){for(var B=arguments[0],C=[],A=1;
A<arguments.length;
A++){C.push(arguments[A])
}if("undefined"!=typeof t&&"function"==typeof t[B]){switch(C.length){case 4:return t[B](C[0],C[1],C[2],C[3]);
case 3:return t[B](C[0],C[1],C[2]);
case 2:return t[B](C[0],C[1]);
case 1:return t[B](C[0]);
default:return t[B]()
}}return null
}v.push(arguments)
}var i=this,q={},r={},t=void 0,u=!1,v=[],w=void 0,y={},p={};
i.container=x;
i.id=x.id;
i.getBuffer=function(){return g("jwGetBuffer")
};
i.getContainer=function(){return i.container
};
i.addButton=function(D,E,A,B){try{p[B]=A,g("jwDockAddButton",D,E,"jwplayer('"+i.id+"').callback('"+B+"')",B)
}catch(C){k.log("Could not add dock button"+C.message)
}};
i.removeButton=function(A){g("jwDockRemoveButton",A)
};
i.callback=function(A){if(p[A]){p[A]()
}};
i.forceState=function(A){g("jwForceState",A);
return i
};
i.releaseState=function(){return g("jwReleaseState")
};
i.getDuration=function(){return g("jwGetDuration")
};
i.getFullscreen=function(){return g("jwGetFullscreen")
};
i.getHeight=function(){return g("jwGetHeight")
};
i.getLockState=function(){return g("jwGetLockState")
};
i.getMeta=function(){return i.getItemMeta()
};
i.getMute=function(){return g("jwGetMute")
};
i.getPlaylist=function(){var A=g("jwGetPlaylist");
"flash"==i.renderingMode&&k.deepReplaceKeyName(A,["__dot__","__spc__","__dsh__","__default__"],["."," ","-","default"]);
return A
};
i.getPlaylistItem=function(A){k.exists(A)||(A=i.getPlaylistIndex());
return i.getPlaylist()[A]
};
i.getPlaylistIndex=function(){return g("jwGetPlaylistIndex")
};
i.getPosition=function(){return g("jwGetPosition")
};
i.getRenderingMode=function(){return i.renderingMode
};
i.getState=function(){return g("jwGetState")
};
i.getVolume=function(){return g("jwGetVolume")
};
i.getWidth=function(){return g("jwGetWidth")
};
i.setFullscreen=function(A){k.exists(A)?g("jwSetFullscreen",A):g("jwSetFullscreen",!g("jwGetFullscreen"));
return i
};
i.setMute=function(A){k.exists(A)?g("jwSetMute",A):g("jwSetMute",!g("jwGetMute"));
return i
};
i.lock=function(){return i
};
i.unlock=function(){return i
};
i.load=function(A){g("jwLoad",A);
return i
};
i.playlistItem=function(A){g("jwPlaylistItem",parseInt(A));
return i
};
i.playlistPrev=function(){g("jwPlaylistPrev");
return i
};
i.playlistNext=function(){g("jwPlaylistNext");
return i
};
i.resize=function(C,D){if("flash"!=i.renderingMode){var A=document.getElementById(i.id);
A.className=A.className.replace(/\s+aspectMode/,"");
A.style.display="block";
g("jwResize",C,D)
}else{var A=a.getElementById(i.id+"_wrapper"),B=a.getElementById(i.id+"_aspect");
B&&(B.style.display="none");
A&&(A.style.display="block",A.style.width=k.styleDimension(C),A.style.height=k.styleDimension(D))
}return i
};
i.play=function(A){"undefined"==typeof A?(A=i.getState(),A==h.PLAYING||A==h.BUFFERING?g("jwPause"):g("jwPlay")):g("jwPlay",A);
return i
};
i.pause=function(A){"undefined"==typeof A?(A=i.getState(),A==h.PLAYING||A==h.BUFFERING?g("jwPause"):g("jwPlay")):g("jwPause",A);
return i
};
i.stop=function(){g("jwStop");
return i
};
i.seek=function(A){g("jwSeek",A);
return i
};
i.setVolume=function(A){g("jwSetVolume",A);
return i
};
i.loadInstream=function(A,B){return w=new j.instream(this,t,A,B)
};
i.getQualityLevels=function(){return g("jwGetQualityLevels")
};
i.getCurrentQuality=function(){return g("jwGetCurrentQuality")
};
i.setCurrentQuality=function(A){g("jwSetCurrentQuality",A)
};
i.getCaptionsList=function(){return g("jwGetCaptionsList")
};
i.getCurrentCaptions=function(){return g("jwGetCurrentCaptions")
};
i.setCurrentCaptions=function(A){g("jwSetCurrentCaptions",A)
};
i.getControls=function(){return g("jwGetControls")
};
i.getSafeRegion=function(){return g("jwGetSafeRegion")
};
i.setControls=function(A){g("jwSetControls",A)
};
i.destroyPlayer=function(){g("jwPlayerDestroy")
};
i.playAd=function(A){g("jwPlayAd",A)
};
var z={onBufferChange:f.JWPLAYER_MEDIA_BUFFER,onBufferFull:f.JWPLAYER_MEDIA_BUFFER_FULL,onError:f.JWPLAYER_ERROR,onSetupError:f.JWPLAYER_SETUP_ERROR,onFullscreen:f.JWPLAYER_FULLSCREEN,onMeta:f.JWPLAYER_MEDIA_META,onMute:f.JWPLAYER_MEDIA_MUTE,onPlaylist:f.JWPLAYER_PLAYLIST_LOADED,onPlaylistItem:f.JWPLAYER_PLAYLIST_ITEM,onPlaylistComplete:f.JWPLAYER_PLAYLIST_COMPLETE,onReady:f.API_READY,onResize:f.JWPLAYER_RESIZE,onComplete:f.JWPLAYER_MEDIA_COMPLETE,onSeek:f.JWPLAYER_MEDIA_SEEK,onTime:f.JWPLAYER_MEDIA_TIME,onVolume:f.JWPLAYER_MEDIA_VOLUME,onBeforePlay:f.JWPLAYER_MEDIA_BEFOREPLAY,onBeforeComplete:f.JWPLAYER_MEDIA_BEFORECOMPLETE,onDisplayClick:f.JWPLAYER_DISPLAY_CLICK,onControls:f.JWPLAYER_CONTROLS,onQualityLevels:f.JWPLAYER_MEDIA_LEVELS,onQualityChange:f.JWPLAYER_MEDIA_LEVEL_CHANGED,onCaptionsList:f.JWPLAYER_CAPTIONS_LIST,onCaptionsChange:f.JWPLAYER_CAPTIONS_CHANGED,onAdError:f.JWPLAYER_AD_ERROR,onAdClick:f.JWPLAYER_AD_CLICK,onAdImpression:f.JWPLAYER_AD_IMPRESSION,onAdTime:f.JWPLAYER_AD_TIME,onAdComplete:f.JWPLAYER_AD_COMPLETE,onAdCompanions:f.JWPLAYER_AD_COMPANIONS};
k.foreach(z,function(A){i[A]=b(z[A],n)
});
var c={onBuffer:h.BUFFERING,onPause:h.PAUSED,onPlay:h.PLAYING,onIdle:h.IDLE};
k.foreach(c,function(A){i[A]=b(c[A],m)
});
i.remove=function(){if(!u){throw"Cannot call remove() before player is ready"
}v=[];
j.destroyPlayer(this.id)
};
i.setup=function(A){if(o.embed){var B=a.getElementById(i.id);
B&&(A.fallbackDiv=B);
B=i;
v=[];
j.destroyPlayer(B.id);
B=o(i.id);
B.config=A;
return new o.embed(B)
}return i
};
i.registerPlugin=function(C,D,A,B){o.plugins.registerPlugin(C,D,A,B)
};
i.setPlayer=function(A,B){t=A;
i.renderingMode=B
};
i.detachMedia=function(){if("html5"==i.renderingMode){return g("jwDetachMedia")
}};
i.attachMedia=function(A){if("html5"==i.renderingMode){return g("jwAttachMedia",A)
}};
i.dispatchEvent=function(D,E){if(q[D]){for(var A=k.translateEventResponse(D,E),B=0;
B<q[D].length;
B++){if("function"==typeof q[D][B]){try{D==f.JWPLAYER_PLAYLIST_LOADED&&k.deepReplaceKeyName(A.playlist,["__dot__","__spc__","__dsh__","__default__"],["."," ","-","default"]),q[D][B].call(this,A)
}catch(C){k.log("There was an error calling back an event handler")
}}}}};
i.dispatchInstreamEvent=function(A){w&&w.dispatchEvent(A,arguments)
};
i.callInternal=g;
i.playerReady=function(A){u=!0;
t||i.setPlayer(a.getElementById(A.id));
i.container=a.getElementById(i.id);
k.foreach(q,function(B){l(t,B)
});
n(f.JWPLAYER_PLAYLIST_ITEM,function(){y={}
});
n(f.JWPLAYER_MEDIA_META,function(B){k.extend(y,B.metadata)
});
for(i.dispatchEvent(f.API_READY);
0<v.length;
){g.apply(this,v.shift())
}};
i.getItemMeta=function(){return y
};
i.isBeforePlay=function(){return t.jwIsBeforePlay()
};
i.isBeforeComplete=function(){return t.jwIsBeforeComplete()
};
return i
};
j.selectPlayer=function(b){var c;
k.exists(b)||(b=0);
b.nodeType?c=b:"string"==typeof b&&(c=a.getElementById(b));
return c?(b=j.playerById(c.id))?b:j.addPlayer(new j(c)):"number"==typeof b?d[b]:null
};
j.playerById=function(b){for(var c=0;
c<d.length;
c++){if(d[c].id==b){return d[c]
}}return null
};
j.addPlayer=function(b){for(var c=0;
c<d.length;
c++){if(d[c]==b){return b
}}d.push(b);
return b
};
j.destroyPlayer=function(b){for(var c=-1,g,i=0;
i<d.length;
i++){d[i].id==b&&(c=i,g=d[i])
}0<=c&&(b=g.id,i=a.getElementById(b+("flash"==g.renderingMode?"_wrapper":"")),k.clearCss&&k.clearCss("#"+b),i&&("html5"==g.renderingMode&&g.destroyPlayer(),g=a.createElement("div"),g.id=b,i.parentNode.replaceChild(g,i)),d.splice(c,1));
return null
};
o.playerReady=function(c){var b=o.api.playerById(c.id);
b?b.playerReady(c):o.api.selectPlayer(c.id).playerReady(c)
}
}(jwplayer),function(d){var a=d.events,h=d.utils,f=a.state;
d.api.instream=function(b,c,j,v){function w(i,k){l[i]||(l[i]=[],p.jwInstreamAddEventListener(i,'function(dat) { jwplayer("'+m.id+'").dispatchInstreamEvent("'+i+'", dat); }'));
l[i].push(k);
return this
}function n(k,i){g[k]||(g[k]=[],w(a.JWPLAYER_PLAYER_STATE,function(o){var q=o.newstate,r=o.oldstate;
if(q==k){var t=g[q];
if(t){for(var u=0;
u<t.length;
u++){"function"==typeof t[u]&&t[u].call(this,{oldstate:r,newstate:q,type:o.type})
}}}}));
g[k].push(i);
return this
}var m=b,p=c,l={},g={};
this.dispatchEvent=function(k,o){if(l[k]){for(var q=h.translateEventResponse(k,o[1]),i=0;
i<l[k].length;
i++){"function"==typeof l[k][i]&&l[k][i].call(this,q)
}}};
this.onError=function(i){return w(a.JWPLAYER_ERROR,i)
};
this.onFullscreen=function(i){return w(a.JWPLAYER_FULLSCREEN,i)
};
this.onMeta=function(i){return w(a.JWPLAYER_MEDIA_META,i)
};
this.onMute=function(i){return w(a.JWPLAYER_MEDIA_MUTE,i)
};
this.onComplete=function(i){return w(a.JWPLAYER_MEDIA_COMPLETE,i)
};
this.onTime=function(i){return w(a.JWPLAYER_MEDIA_TIME,i)
};
this.onBuffer=function(i){return n(f.BUFFERING,i)
};
this.onPause=function(i){return n(f.PAUSED,i)
};
this.onPlay=function(i){return n(f.PLAYING,i)
};
this.onIdle=function(i){return n(f.IDLE,i)
};
this.onClick=function(i){return w(a.JWPLAYER_INSTREAM_CLICK,i)
};
this.onInstreamDestroyed=function(i){return w(a.JWPLAYER_INSTREAM_DESTROYED,i)
};
this.play=function(i){p.jwInstreamPlay(i)
};
this.pause=function(i){p.jwInstreamPause(i)
};
this.destroy=function(){p.jwInstreamDestroy()
};
this.setText=function(i){p.jwInstreamSetText(i?i:"")
};
m.callInternal("jwLoadInstream",j,v?v:{})
}
}(jwplayer),function(d){var a=d.api,f=a.selectPlayer;
a.selectPlayer=function(b){return(b=f(b))?b:{registerPlugin:function(k,c,j){d.plugins.registerPlugin(k,c,j)
}}
}
}(jwplayer));
jwplayer.key="uG/VHSbjrT7/udRHL0vnyr5GjyFu3WZQ9+VRUxia1vs=";
if(typeof String.prototype.startsWith!="function"){String.prototype.startsWith=function(a){return this.slice(0,a.length)===a
}
}$(function(){$(".conv3_footer .listcon .menu_foot_products").on("click",function(){var d=$(this).attr("wrap");
if(!d){return
}var b="open";
var a="footer:menu:explore";
var c="phones:all phones";
if(d.startsWith("menu_module_")){d=d.replace("menu_module_","");
c="more products:"+d
}analyticsSubmit(a,b,c,EVENT_TYPE_OPEN_MENU_SECOND_LEVEL)
})
});
window.viewType=function(){var a=window.innerWidth||$(window).width();
return a>=1024?"pc":(a<768?"mobile":"tablet")
};
$.fn.initJwplayer=function(c){var g=$(this),a={path:"../",target:"self",autostart:false};
var f=null,d=g.data("t-lab"),b=$.isAndroid();
window.conv3VidoeControl=window.conv3VidoeControl||{};
$.extend(a,c);
return this.each(function(o){var k=0;
var m=false;
var t=function(w,x){switch(x){case"show":w.find("video").show();
w.find(".jwpreview").css({opacity:0,visibility:"hidden"});
w.find(".jwcontrolbar").show();
break;
case"hide":w.find("video").hide();
w.find(".jwpreview").css({opacity:1,visibility:"visible"});
w.find(".jwcontrolbar").hide();
break
}};
var r=$(this).data("t-viewtimes");
var n=false;
var j={id:$(this).data("video-id"),image:$(this).data("video-image"),link:$(this).data("video-link"),aspectratio:$(this).data("video-ratio"),file:$(this).attr("href"),width:"100%",label:$(this).data("t-label"),autostart:a.autostart,flashplayer:"/etc/designs/huawei-cbg-site/statics/hw_jwflash.swf",tracks:[{file:$(this).data("video-track"),label:"on",kind:"captions","default":true}],captions:{back:false,color:$(this).data("caption-color")||"ffffff",fontsize:15},events:{onReady:function(){},onPlay:function(w){$(".jwdisplay").removeClass("x-mask");
$(".jwpreview").removeClass("x-opacity");
$(".jwplayer .x-over").hide();
clearTimeout(f);
if(!g.data("video-start")){$.trackVideo("Video Milestone","start",j.label+","+queryVariable("<URL>"));
g.data("video-start",true)
}else{$.trackVideo("Video Play/Pause/Exit","play",j.label+","+queryVariable("<URL>"))
}m=true;
clearTimeout(q);
b&&t(l,"show")
},onPause:function(){b&&t(l,"hide")
},onComplete:function(){$(".jwdisplay").addClass("x-mask");
$(".jwpreview").addClass("x-opacity");
$(".jwplayer .x-over").show();
m=false;
clearTimeout(q);
b&&t(l,"hide")
}}};
var l=null,q=null;
var i=function(){jwplayer(j.id).pause(true);
m=false;
clearTimeout(q);
q=setTimeout(function(){j.events.onPause()
},100)
};
conv3VidoeControl.pause=conv3VidoeControl.pause||[];
conv3VidoeControl.pause.push(i);
if(b){$(window).on("scroll",function(){if(m){i()
}})
}if($("html").hasClass("ie9")||$("html").hasClass("ie8")||$("html").hasClass("ie7")){j.primary="flash"
}else{j.primary="html5"
}var h=1600,v=900;
if(typeof(j.aspectratio)=="string"&&/^[0-9]{1,2}:[0-9]{1,2}$/.test(j.aspectratio)){var p=j.aspectratio.split(":");
v=h*parseInt(p[1])/parseInt(p[0])
}if(a.target=="self"){$(this).html('<div id="'+j.id+'"></div>');
try{jwplayer(j.id).setup(j);
if(r){jwplayer(j.id).onPlay(function(x){if(n){return
}var w=window.digitalData.page.pageInfo.uri.split("/").reverse()[1].split(".")[0];
addStatistics(w);
n=true
})
}jwplayer(j.id).onReady(function(w){l=$("#"+j.id)
})
}catch(o){}}else{if(a.target=="fancybox"){var u=function(w){w.stopPropagation();
w.preventDefault();
return false
};
$("head").append('<link href="/etc/designs/huawei-cbg-site/statics/jquery.fancybox-v2.1.5.css" rel="stylesheet" type="text/css" />');
$.getScript("/etc/designs/huawei-cbg-site/statics/lib-bundle.js",function(){$.fancybox('<div id="'+j.id+'" class="cbg-jwplayer"></div><div class="cbg-video-mask"></div>',{width:h,height:v,padding:0,margin:20,autoSize:false,aspectRatio:true,scrolling:"no",beforeShow:function(){try{if(g.data("iframe-url")){var y='<iframe height="100%" width="100%" src="'+g.data("iframe-url")+'?autoplay=1" frameborder=0 allowfullscreen></iframe>';
$(".fancybox-wrap #videoPlayer").remove();
$(".fancybox-wrap .fancybox-inner").prepend(y)
}else{jwplayer(j.id).setup(j);
jwplayer(j.id).onFullscreen(function(B){B.fullscreen?$(".fancybox-close").hide():$(".fancybox-close").show();
!B.fullscreen&&$(".jwcontrolbar").css({opacity:0,display:"inline-block"})
});
jwplayer(j.id).onReady(function(B){$(".cbg-video-mask").fadeOut();
l=$("#"+j.id)
});
$(".fancybox-overlay").on("touchmove",u);
$("#cbg-banner").flexslider("pause")
}}catch(z){}if(window.innerWidth<1024){var w=$(window).height(),x=$(".fancybox-inner").height(),A=parseFloat((w-x)/2);
$(".fancybox-wrap").css("top",A);
_scrollTop=$(document).scrollTop();
$("html,body").css({height:$(window).height(),overflow:"hidden"}).scrollTop(_scrollTop);
return _scrollTop
}},afterClose:function(){$("[data-video-id]").removeClass("active");
if(window.innerWidth<1024){$("html,body").removeAttr("style").scrollTop(_scrollTop)
}},beforeClose:function(){var x=g.data("video-name")||"<video name>";
var y="<product name> - "+x+" - <page title>";
if(g.data("iframe-url")){}else{jwplayer(0).stop();
jwplayer(j.id).stop();
var w=Math.floor(jwplayer(j.id).getPosition()*100/jwplayer(j.id).getDuration())
}window.dataLayer.push(addATCommonFields({event:"video",videoStep:"close",videoName:x,productMktName:pageProductInfo&&pageProductInfo.marketingName||"",productCategory:pageProductInfo&&pageProductInfo.category||"",clickName:"video "+x+"_close",clickType:"action"}))
}})
})
}}})
};
var videotrack=new Array();
$.fn.initH5player=function(b){var c=$(this),a={path:"../",target:"self",autostart:false};
$.extend(a,b);
return this.each(function(m){var f={id:$(this).data("video-id"),image:$(this).data("video-image"),aspectratio:$(this).data("video-ratio"),file:$(this).attr("href"),tracks:$(this).data("video-track")};
var o={};
o.endedEventTime=0;
o.playPercentTime_25=0;
o.playPercentTime_50=0;
o.playPercentTime_75=0;
var j=pageProductInfo&&pageProductInfo.marketingName||"";
var w=pageProductInfo&&pageProductInfo.category||"";
if(addVideoList(f.file)){videotrack.push(f)
}var r=[];
for(var k=0;
k<videotrack.length;
k++){if(videotrack[k].file==f.file){r=videotrack[k];
break
}}var h=c.data("video-name");
var q=digitalData.product?digitalData.product.productInfo.marketingName:"";
f.label=q===""?h+" - "+digitalData.page.pageInfo.pageName:q+" - "+h+" - "+digitalData.page.pageInfo.pageName;
if($(this).data("t-label")){f.label=$(this).data("t-label")
}var d=b.width||1600,u=b.height||900;
var d=1600,u=900;
if(typeof(f.aspectratio)=="string"&&/^[0-9]{1,2}:[0-9]{1,2}$/.test(f.aspectratio)){var n=f.aspectratio.split(":");
u=d*parseInt(n[1])/parseInt(n[0])
}if(f.tracks){var t="<video controls  playsinline='true' webkit-playsinline='true' controlsList='nodownload' poster='"+f.image+"' id='"+f.id+"' style='width:100%;height:auto'><source src='"+f.file+"' type='video/mp4' /><track src='"+f.tracks+"' kind='subtitles' default />Your browser does not support mp4 video.</video>"
}else{var t="<video controls  playsinline='true' webkit-playsinline='true' controlsList='nodownload' poster='"+f.image+"' id='"+f.id+"' style='width:100%;height:auto'><source src='"+f.file+"' type='video/mp4' /></video>"
}if(a.target=="self"){$(this).html('<div class="self-video">'+t+"</div>");
var l=1000;
var g=setInterval(function(){var v=$("#"+f.id);
var i=v[0];
if(v.length>0&&i.readyState=="4"){i.play();
handleGAInVideoEventListener(i,f.label,o,j,w);
clearInterval(g)
}if(l--<1){clearInterval(g)
}},100)
}else{if(a.target=="fancybox"){var p=function(i){i.stopPropagation();
i.preventDefault();
return false
};
$("head").append('<link href="/etc/designs/huawei-cbg-site/statics/jquery.fancybox-v2.1.5.css" rel="stylesheet" type="text/css" />');
$.getScript("/etc/designs/huawei-cbg-site/statics/lib-bundle.js",function(){$.fancybox('<div class="cbg-jwplayer">'+t+'</div><div class="cbg-video-mask"></div>',{width:d,height:u,padding:0,margin:20,autoSize:false,aspectRatio:true,scrolling:"no",beforeShow:function(){var i=1000;
var v=setInterval(function(){var y=$("#"+f.id);
var x=y[0];
if(y.length>0&&x.readyState=="4"){x.play();
handleGAInVideoEventListener(x,f.label,o,j,w);
clearInterval(v)
}if(i--<1){clearInterval(v)
}},100)
},afterClose:function(){},beforeClose:function(){var v=$("#"+f.id);
var i=v[0];
i.currentTime=0;
closeAllVideo(f.id);
pushVideoDatalayer(f.label,"close",j,w)
}})
})
}}})
};
function handleGAInVideoEventListener(c,b,d,f,a){if(d==null){return false
}pushVideoDatalayer(b,"play",f,a);
c.onended=function(g){if(d.endedEventTime==0){d.endedEventTime=1;
pushVideoDatalayer(b,"100%",f,a)
}};
c.onpause=function(g){if(c.currentTime==0||c.currentTime==c.duration){return false
}pushVideoDatalayer(b,"pause",f,a)
};
c.ontimeupdate=function(){videoStepHandleGaEvent(c,b,d,f,a)
}
}function videoStepHandleGaEvent(c,b,d,g,a){var f=Math.floor(c.currentTime*100/c.duration);
if(f>=25&&f<50&&d.playPercentTime_25==0){pushVideoDatalayer(b,"25%",g,a);
d.playPercentTime_25=1
}else{if(f>=50&&f<75&&d.playPercentTime_50==0){pushVideoDatalayer(b,"50%",g,a);
d.playPercentTime_50=1
}else{if(f>=75&&f<100&&d.playPercentTime_75==0){pushVideoDatalayer(b,"75%",g,a);
d.playPercentTime_75=1
}}}}function addVideoList(c){var a=videotrack.length;
for(var b=0;
b<a;
b++){if(videotrack[b].file==c){return false
}}return true
}function closeAllVideo(a){document.getElementById(a).pause()
}(function(a){a.fn.addSelector=function(c){var d=a(this);
var b={tabView:undefined,tabClass:"current",tabChangeTitle:true};
var f=function(){return b.tabView=="both"||(b.tabView&&b.tabView.indexOf(viewType())>-1)
};
a.extend(b,c);
d.find(".select").on("click",function(k){if(f()){return
}var l=a(this),i=l.find("ol"),j=l.siblings(".select");
var h=i.find("li");
if((l.parents(".add-contact-info").length>0||l.parents(".user-perfect-dialog").length>0)&&h.length==0){return
}if(l.hasClass("disable")){return
}if(i.data("slide")=="open"){i.slideUp(250,function(){i.data("slide","close")
});
setTimeout(function(){l.find("span").removeClass("active")
},250)
}else{i.slideDown(250,function(){i.data("slide","open")
});
l.find("span").addClass("active")
}j.find("ol").slideUp(250,function(){a(this).data("slide","close")
});
j.find("span").removeClass("active");
if(l.parents(".add-contact-info").length>0||l.parents(".user-perfect-dialog").length>0){var g=l.parents(".s-selector").siblings(".s-selector");
g.find("ol").slideUp(250,function(){a(this).data("slide","close")
});
g.find("span").removeClass("active")
}k.stopPropagation()
});
d.find(".select ol li").off("click.compareItem").on("click.compareItem",function(k){var g=a(this),i=g.parents(".select").eq(0).find("span"),h=g.text(),j=i.text();
if(f()){g.addClass(b.tabClass).siblings("li").removeClass(b.tabClass)
}else{g.addClass(b.tabClass).siblings("li").removeClass(b.tabClass);
g.parents(".select").eq(0).find("ol").slideUp(250,function(){a(this).data("slide","close")
})
}b.tabChangeTitle&&i.text(h);
d.trigger("selected",{val:h,_mark:g.parents("ol").eq(0).attr("_mark")});
setTimeout(function(){a(".conv3_search_wrap .result_news_pc .list li strong").each(function(){var l=a(this).find("a");
if(l.height()>45){a(this).addClass("ellipsis")
}});
a(".conv3_search_wrap .result_news_pc .list li p").each(function(){var l=a(this).find("span.content");
if(l.height()>65){a(this).addClass("ellipsis")
}})
},500);
k.stopPropagation();
setTimeout(function(){i.removeClass("active")
},250)
});
a("body").on("click",function(){if(f()){return
}var g=d.find(".select");
g.find("ol").slideUp(250,function(){a(this).data("slide","close")
});
setTimeout(function(){g.find("span").removeClass("active")
},250)
});
if(f()){a(window).on("resize",function(){if(f()){d.find(".select ol").show()
}else{d.find(".select ol").hide()
}})
}return d
}
})(jQuery);
function RenderSelectInput(i,g,h){var b=parseInt($(i).css("width").replace("px",""));
var f=parseInt($(i).css("height").replace("px",""));
var c=$(i).children("span").first();
c.after("<input type='text' class='select-input' placeholder='"+g+"' />");
var a=$(i).children("input").first();
var d=$(i).children("ol").first();
c.css("font-size","0");
a.css({height:f+"px",position:"relative",display:"block",left:"0",top:"-"+f+"px",outline:"none","border-width":"0","background-color":"transparent","margin-left":"auto","margin-right":"auto",width:$(c).css("width")});
a.keyup(function(){if(h!="undefined"){h(a,function(){d.children("li").each(function(){if($(this).text().toUpperCase().indexOf($(a).val().toUpperCase())>=0){$(this).html($(this).text().replace($(a).val().toUpperCase(),"<strong style='color:red;' >"+$(a).val().toUpperCase()+"</strong>"));
$(this).show()
}else{$(this).hide()
}});
if(!$(c).hasClass("active")){$(c).addClass("active")
}setTimeout(function(){$(d).css("display","block")
},500)
})
}});
a.focus(function(j){if(a.val()==""){return
}if(!$(c).hasClass("active")){$(c).addClass("active")
}setTimeout(function(){$(d).css("display","block")
},500)
});
$(window).resize(function(){a.css({width:$(c).css("width")})
});
$(i+" ol").first().find("li").on("click",function(){$(a).val($(this).text());
$(i+" ol").first().hide()
});
window.SelectProduct=function(j){setTimeout(function(){$(".conv3_certification_wrap .conv3_global_selector .select input").first().val(j);
$(".conv3_global_selector .select ol").hide()
},200)
}
}$.isAndroid=function(){return navigator.userAgent.indexOf("Android")>-1||navigator.userAgent.indexOf("Adr")>-1
};
$.isIos=function(){return !!navigator.userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)
};
$.isMobile=function(){var a=navigator.userAgent;
var c=new Array("Android","iPhone","SymbianOS","Windows Phone","iPad","iPod");
for(var b=0;
b<c.length;
b++){if(a.indexOf(c[b])>0){return true
}}return false
};
$.isPc=function(){return !$.isMobile()
};
$.equip=function(){var a=navigator.userAgent;
var c=new Array("Android","iPhone","SymbianOS","Windows Phone","iPad","iPod");
for(var b=0;
b<c.length;
b++){if(a.indexOf(c[b])>0){return c[b]
}}return"pc"
};
function HeightKey(d,i,j){var f=d;
var g=i;
var h=(f&&g)?f.toLowerCase().indexOf(g.toLowerCase()):-1;
if(h>-1){if(h==0){var c="<"+j+">"+f.substring(0,g.length)+"</"+j+">";
var b=f.substring(g.length,f.length);
var a=""
}else{var c=f.substring(0,h);
var b="<"+j+">"+f.substring(h,g.length+h)+"</"+j+">";
var a=f.substring(g.length+h,d.length)
}f=c+b+a
}return f
}function getURLParam(b){var a=decodeURIComponent(window.location.href).match(new RegExp("[?&]"+b+"=([^=&]*)(&|$)"));
return a?a[1]:null
}var monthtxt=$("#month_txt").val();
if(monthtxt==""||monthtxt=="month txt"){monthtxt="January,February,March,April,May,June,July,August,September,October,November,December"
}var montharray=monthtxt.split(",");
function formatMonth(b){var a=parseInt(b);
return montharray[a-1]
}function formatTime(d,c){if(d&&d!=""){var b=d.split("-");
var a=formatMonth(b[1]);
return a+" "+b[2]+", "+b[0]
}else{return""
}}function deleteHttp(a){if(a!=null&&typeof a=="string"){if(a.indexOf("http:")==0){return a.substring(5,a.length)
}else{if(a.indexOf("https:")==0){return a.substring(6,a.length)
}else{return a
}}}else{return a
}}function formatString(a){if(a){return a
}return""
}function getVideoActionStatus(a){if(a<25){return"Video Start"
}if(a<50){return"Video 25%"
}if(a<75){return"Video 50%"
}if(a<99){return"Video 75%"
}return"Video Complete"
}function setCookie(a,c){var b=7;
var d=new Date();
d.setTime(d.getTime()+b*24*60*60*1000);
document.cookie=a+"="+escape(c)+";expires="+d.toGMTString()+";path=/"
}function getCookie(b){var a,c=new RegExp("(^| )"+b+"=([^;]*)(;|$)");
if(a=document.cookie.match(c)){return unescape(a[2])
}else{return null
}}function delCookie(a){var c=new Date();
c.setTime(c.getTime()-1);
var b=getCookie(a);
if(b!=null){document.cookie=a+"="+b+";expires="+c.toGMTString()
}}function getExplorerInfo(){var b=window.navigator.userAgent.toLowerCase();
if(b.indexOf("msie")>=0){var a=b.match(/msie ([\d.]+)/)[1];
return{type:"IE",version:a}
}else{if(b.indexOf("Edge")>=0){var a=b.match(/Edge\/([\d.]+)/)[1];
return{type:"Edge",version:a}
}else{if(b.indexOf("firefox")>=0){var a=b.match(/firefox\/([\d.]+)/)[1];
return{type:"Firefox",version:a}
}else{if(b.indexOf("chrome")>=0){var a=b.match(/chrome\/([\d.]+)/)[1];
return{type:"Chrome",version:a}
}else{if(b.indexOf("opera")>=0){var a=b.match(/opera.([\d.]+)/)[1];
return{type:"Opera",version:a}
}else{if(b.indexOf("safari")>=0){return{type:"Safari",version:0}
}else{return{type:0,version:0}
}}}}}}}function snsShare(d,b){var a=b||document.location.href;
var c=encodeURIComponent(document.title);
var f="";
switch(d){case"facebook":f="https://www.facebook.com/sharer/sharer.php?u="+a;
break;
case"googleplus":f="https://plus.google.com/u/0/share?text="+c+encodeURIComponent(" ")+a;
break;
case"twitter":f="https://twitter.com/intent/tweet?text="+c+encodeURIComponent(" ")+a;
break;
case"sinablog":f="http://v.t.sina.com.cn/share/share.php?url="+a+"&title="+c+"&appkey=330242870";
break;
case"qqblog":f="http://shuqian.qq.com/post?from=3&title="+c+"&uri="+encodeURIComponent(document.location.href)+"&jumpback=2&noui=1";
break;
default:f=""
}window.open(f,d,"toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=800,height=500,location=1")
}var basesupport="//consumer.huawei.com/support/services/";
function setInitMap(d,g){var f=d.address==undefined?"beijing":d.address;
d.geocoder.geocode({address:d.address},function(a,c){if(c==google.maps.GeocoderStatus.OK){var h={zoom:10,center:a[0].geometry.location,mapTypeId:google.maps.MapTypeId.ROADMAP};
var b=new google.maps.Map(document.getElementById(d.id),h);
g&&g(b)
}})
}function loadMapScript(c){c=c||"en";
var d=document.createElement("script");
d.type="text/javascript";
d.setAttribute("async","");
d.setAttribute("defer","");
d.src="//maps.google.com/maps/api/js?key=AIzaSyB5ykZNED0-oT4i1RZRqS9oetClB7wCwfE&language="+c.toLowerCase()+"&callback=initMap";
document.body.appendChild(d)
}var MenuPageHistory=function(b){function a(c){this.pages=[];
this.option=c;
this.closeCallBack;
this.prePushCallBack
}a.prototype.PushPage=function(c,f){var d=this;
d.prePushCallBack&&d.prePushCallBack();
setTimeout(function(){if(d.pages.length>0){var g=d.pages[d.pages.length-1];
d.pages.push(c);
b(g).slideUp(d.option.slideSpeed,function(){b(c).slideDown(d.option.slideSpeed,function(){f&&f()
})
})
}else{d.pages.push(c);
b(c).slideDown(d.option.slideSpeed,function(){f&&f()
})
}},200)
};
a.prototype.PopPage=function(f){var d=this;
if(this.pages.length>1){var c=this.pages[this.pages.length-1];
var g=this.pages[this.pages.length-2];
b(c).slideUp(this.option.slideSpeed,function(){b(g).slideDown(d.option.slideSpeed,function(){d.pages.splice(d.pages.length-1,1);
f&&f()
})
})
}else{if(this.pages.length==1){var c=this.pages[this.pages.length-1];
b(c).slideUp(this.option.slideSpeed,function(){d.pages.splice(d.pages.length-1,1);
f&&f();
if(d.pages.length==0){d.closeCallBack&&d.closeCallBack()
}})
}}};
a.prototype.ClosePage=function(f){var d=this;
try{var c=this.pages[this.pages.length-1];
if(!c){f&&f();
return
}b(c).slideUp(this.option.slideSpeed,function(){d.pages.splice(0,d.pages.length);
f&&f();
d.closeCallBack&&d.closeCallBack()
})
}catch(g){f&&f()
}};
a.prototype.CloseHandler=function(c){if(c){this.closeCallBack=c
}};
a.prototype.BeforePushPageHandler=function(c){if(c){this.prePushCallBack=c
}};
return a
}(jQuery);
var slideSpeed=250;
var fotterScrollTop=0;
var menuPageHistory=new MenuPageHistory({slideSpeed:slideSpeed});
menuPageHistory.BeforePushPageHandler(function(){if(fotterScrollTop==0){fotterScrollTop=$(document).scrollTop()
}$(document).scrollTop(0)
});
menuPageHistory.CloseHandler(function(){$("#normal_nav .navcon .menu ul li").removeClass("current");
$(document).scrollTop(fotterScrollTop);
fotterScrollTop=0
});
$(function(){var a=getExplorerInfo();
setTimeout(function(){$("img").each(function(b){$(this).attr("onerror","imgErrorUrl(this)")
})
},3000)
});
var imgErrorUrl=function(a){var b=$(a)||$(this);
var c="/etc/designs/huawei-cbg-site/clientlib-v3/images/hw-logo1-80.png";
if(b.hasClass("imgerror-defaultlogo")){return
}else{b.attr("src",c).addClass("imgerror-defaultlogo")
}};
function clickLazyImgs(a){a.find("img.lazy_src").each(function(){$(this).attr("src",$(this).data("src")).removeClass("lazy_src").show()
})
}function scrollLazyImgs(c,b){var d=parseInt($(document).scrollTop());
var a=parseInt(c.offset().top)-(b||200);
if(d>=a){c.find("img.scroll_src").each(function(f){$(this).attr("src",$(this).data("src")).removeClass("scroll_src").show()
})
}}function classLazy(b,d){var c=d||500;
var a=parseInt($(document).scrollTop())+c;
$(".lazy_class").each(function(){var f=$(this).offset().top;
a>=f?$(this).addClass($(this).data("class")).removeClass("lazy_class"):""
})
}$(function(){$(".part_description,.spec-contect p").each(function(){if($(this).text().indexOf("≥")!=-1){$(this).text($(this).text().replace(/≥/g,">="))
}if($(this).text().indexOf("≤")!=-1){$(this).text($(this).text().replace(/≤/g,"<="))
}})
});
function getV3PageTypeByCategory(a){switch(a){case"phones":return"phones";
case"laptops":return"laptops";
case"tablets":return"tablets";
case"wearables":return"wearables";
case"smart-home":return"smart-home";
case"mobile-broadband":return"more-products";
case"accessories":return"more-products";
case"about-us":return"setCurrentNav";
case"legal":return"setCurrentNav";
case"store-finder":return"setCurrentNav";
default:return"0"
}}function setV3CurrentNav(){var a=$(".header-wrap>.nav-wrap>.left-box>ul>li");
var f=a.length;
var c=getV3PageTypeByCategory(digitalData.page.category.primaryCategory);
var g=digitalData.page.category.pageType;
var h=digitalData.page.category.primaryCategory;
if(g=="support"){for(var d=f-1;
d>0;
d--){if(a.eq(d).find("a").attr("href")&&a.eq(d).find("a").attr("href").indexOf("/support")>0){a.eq(d).addClass("curpage");
break
}}}else{if(h=="emui"){for(var d=f-1;
d>0;
d--){if(a.eq(d).find("a").attr("href")&&a.eq(d).find("a").attr("href").indexOf("/emui")>0){a.eq(d).addClass("curpage");
break
}}}else{if(c!="0"&&c!="setCurrentNav"){var b=0;
for(var d=0;
d<f;
d++){if(a.eq(d).attr("wrap")==c){a.eq(d).addClass("curpage");
b=1;
break
}}b==0?$(".header-wrap>.nav-wrap>.left-box>ul>li[wrap='more-products']").addClass("curpage"):""
}}}}$(document).ready(function(){if($(window).width()>767){setV3CurrentNav()
}$("input[type='text']").each(function(b,a){var c=$(a);
if(!c.attr("maxlength")){c.attr("maxlength",500)
}})
});
var plphidedataToJson=function(){var a=[];
$(".plphidedata_arr span").each(function(b,c){if($(c).text().length>0){a.push(JSON.parse($(c).text().trim()))
}});
return a
};
String.format=function(){var c=arguments[0];
for(var a=0;
a<arguments.length-1;
a++){var b=new RegExp("\\{"+a+"\\}","gm");
c=c.replace(b,arguments[a+1])
}return c
};
$(function(){$(".play_video").on("click",function(){if(window.innerWidth<1024){var a=setInterval(function(){clearInterval(a);
var c=$(window).height(),d=$(".fancybox-inner").height(),f=parseFloat((c-d)/2);
$(".fancybox-wrap").css("top",f);
_scrollTop=$(document).scrollTop();
$("html,body").scrollTop(_scrollTop);
$("html,body").css({});
$(".fancybox-overlay,.fancybox-close").on("click",function(){$("html,body").removeAttr("style").scrollTop(_scrollTop)
});
return _scrollTop
},500);
$(document).on("click",".fancybox-close",function(){$("html,body").removeAttr("style").scrollTop(_scrollTop)
})
}else{var b=setInterval(function(){if($(".fancybox-mobile.fancybox-opened").length>0){clearInterval(b);
$("body").css("overflow","visible");
$(".fancybox-overlay,.fancybox-close").on("click",function(){$("html,body").css("overflow","visible");
$("body").css("height","auto")
})
}},500)
}})
});
var _scrollTop=0;
var bilingual_site_cookie=getCookie("bilingual_site_cookie")?getCookie("bilingual_site_cookie"):"";
var current_site_code=digitalData.page.pageInfo.siteCode||"";
var current_country_code=digitalData.page.pageInfo.countryCode||"";
var site_code="";
var country_code="";
var cookieArr=[];
var cookieStr="";
var c_flag=false;
var s_flag=false;
var replace_str="";
var cookie_info="";
var path_name=window.location.pathname;
var click_flag=false;
if(path_name.indexOf("/editor.html/content/huawei-cbg-site/")==0){path_name=path_name.replace("/editor.html/content/huawei-cbg-site/","");
if(path_name.indexOf("/")>-1){current_site_code=path_name.split("/")[0]
}else{current_site_code=path_name.split(".")[0]
}}else{if(path_name.indexOf("/content/huawei-cbg-site/")==0){path_name=path_name.replace("/content/huawei-cbg-site/","");
if(path_name.indexOf("/")>-1){current_site_code=path_name.split("/")[0]
}else{current_site_code=path_name.split(".")[0]
}}else{current_site_code=path_name.split("/")[1]
}}$(document).ready(function(){if(window.integrationJsInterface||window.integrationJsInterfaceWebview){return
}var c=$(".site_choose_mask");
if(c.length>0){$("#topTipsBox").prepend(c);
$("#header-v4").addClass("has-top-tips");
var k=$("#is_editor").attr("data-is-editor-mode");
$(".site_choose_mask p span.site_choose_btn").each(function(){if($(this).attr("sitecode")&&$(this).attr("sitecode")==current_site_code){$(this).addClass("current").siblings().addClass("other")
}});
$("a.lang_change").click(function(){if($(this).attr("scode")&&$(this).attr("scode")!=""){c_flag=false;
s_flag=false;
var l=$(this).attr("scode");
site_code=l;
country_code=current_country_code;
cookie_info=country_code+"|"+site_code;
var i="";
if(bilingual_site_cookie!=""){i="Y"
}else{i="N"
}h(cookie_info,site_code,i,"yes")
}});
if(bilingual_site_cookie!=""){site_code=current_site_code;
cookieStr=getCookie("bilingual_site_cookie");
cookieArr=cookieStr.split(",");
for(var d=0;
d<cookieArr.length;
d++){if(cookieArr[d].split("|")[0]==current_country_code){c_flag=true;
replace_str=cookieArr[d];
if(cookieArr[d].split("|")[1]==site_code){s_flag=true
}}}if(c_flag==true&&s_flag==false){site_code=replace_str.split("|")[1];
j(site_code)
}else{if(c_flag==false&&k=="false"){f()
}}}else{if(k=="false"){f()
}}$(document).on("click","#close_btn",function(p){p.stopPropagation();
var i="navigation";
var l="site_language_box_close";
var n=current_site_code;
if(typeof ga=="function"){ga("send","event",i,l,n)
}var m=g()==window.location.href?window.location.href:g();
dmpaCommon("trackEvent","click","pop_up interaction","Close",m);
$("html").removeClass("htmlbody_scroll");
b();
site_code=current_site_code;
country_code=current_country_code;
cookie_info=country_code+"|"+site_code;
var o="";
if(bilingual_site_cookie!=""){o="Y"
}else{o="N"
}h(cookie_info,site_code,o,"yes")
});
function g(){var l=window.location.href;
var i=window.location.origin;
var n=window.location.pathname;
var m=window.location.search;
if(n.indexOf("/editor.html/content/huawei-cbg-site/")==0){n=n.replace("/editor.html/content/huawei-cbg-site/","");
if(n.indexOf("/")>-1){n=n.replace(n.split("/")[0],site_code);
n="/editor.html/content/huawei-cbg-site/"+n;
l=i+n
}else{n=n.replace(n.split(".")[0],site_code);
n="/editor.html/content/huawei-cbg-site/"+n;
l=i+n+m
}}else{if(n.indexOf("/content/huawei-cbg-site/")==0){n=n.replace("/content/huawei-cbg-site/","");
if(n.indexOf("/")>-1){n=n.replace(n.split("/")[0],site_code);
n="/content/huawei-cbg-site/"+n;
l=i+n+m
}else{n=n.replace(n.split(".")[0],site_code);
n="/content/huawei-cbg-site/"+n;
l=i+n+m
}}else{n=n.replace("/"+current_site_code+"/","/"+site_code+"/");
l=i+n+m
}}return l
}$(document).on("click",".site_choose_btn",function(n){n.stopPropagation();
var r="navigation";
var q="site_language_select";
var l=current_site_code+"_"+$(this).text();
if(typeof ga=="function"){ga("send","event",r,q,l)
}var m=$(this).attr("data-language").toLowerCase()=="english"?"English":"Arabic",p=g()==window.location.href?window.location.href:g();
dmpaCommon("trackEvent","click","pop_up interaction",m,p);
var t="yes";
if($(this).hasClass("current")){click_flag=true
}else{click_flag=false
}var o="";
if(bilingual_site_cookie!=""){o="Y"
}else{o="N"
}var i=$(this).attr("siteCode");
if(i){$("html").removeClass("htmlbody_scroll");
b();
site_code=i;
country_code=current_country_code;
cookie_info=country_code+"|"+site_code;
h(cookie_info,site_code,o,t)
}});
function h(l,n,o,p){if(getCookie("bilingual_site_cookie")&&getCookie("bilingual_site_cookie")!=""){cookieStr=getCookie("bilingual_site_cookie");
cookieArr=cookieStr.split(",");
for(var m=0;
m<cookieArr.length;
m++){if(cookieArr[m].split("|")[0]==current_country_code){c_flag=true;
replace_str=cookieArr[m];
if(cookieArr[m].split("|")[1]==n){s_flag=true
}}}if(c_flag==true&&s_flag==true&&p=="yes"){j(n,o,p)
}else{if(c_flag==true&&s_flag==false){cookieStr=cookieStr.replace(replace_str,l);
setCookie("bilingual_site_cookie",cookieStr);
j(n,o,p)
}else{if(c_flag==false){cookieStr=cookieStr+","+l;
setCookie("bilingual_site_cookie",cookieStr);
j(n,o,p)
}}}}else{cookieArr.push(l);
setCookie("bilingual_site_cookie",cookieArr);
j(n,o,"yes")
}}function j(n,o,p){var l=window.location.href;
var i=window.location.origin;
var q=window.location.pathname;
var m=window.location.search;
if(q.indexOf("/editor.html/content/huawei-cbg-site/")==0){q=q.replace("/editor.html/content/huawei-cbg-site/","");
if(q.indexOf("/")>-1){q=q.replace(q.split("/")[0],n);
q="/editor.html/content/huawei-cbg-site/"+q;
l=i+q
}else{q=q.replace(q.split(".")[0],n);
q="/editor.html/content/huawei-cbg-site/"+q;
l=i+q+m
}}else{if(q.indexOf("/content/huawei-cbg-site/")==0){q=q.replace("/content/huawei-cbg-site/","");
if(q.indexOf("/")>-1){q=q.replace(q.split("/")[0],n);
q="/content/huawei-cbg-site/"+q;
l=i+q+m
}else{q=q.replace(q.split(".")[0],n);
q="/content/huawei-cbg-site/"+q;
l=i+q+m
}}else{q=q.replace("/"+current_site_code+"/","/"+n+"/");
l=i+q+m
}}if(p=="yes"){window.location.href=l
}else{if(k=="false"){f()
}}}function f(){c.show();
a()
}function b(){c.hide();
a()
}function a(){var m=$("#header-v4");
var l=$("#header-placeholder");
var i=m.innerHeight();
l.css({height:i});
$(".n12-search").css("top",i);
if(Mkt.Util.windowWidth()<=1199){$(".main-nav").css("top",i);
$(".huawei-v4 .login-v4-wrap .login-v4").css("top",i)
}}}});
$(document).ready(function(){appEmbedded();
IEVersion();
if($(".huawei-convergent-cookie").length>0){showJpCookie();
var a=getCookie("huawei_store_accept_cookie_flag");
if(enableNewCookieCfg&&cookieModeSetting&&cookieModeSetting=="fusionPromptModeB"&&enableDefaultCookieAccept&&!a){cookieBListenClick()
}}else{showCookieTip()
}setHotKeysList();
$(".huawei-ie-tips .huawei-ie-close").on("click",function(){$(".huawei-ie-tips").slideUp(500)
});
$(".huawei-v4 .huawei-cookie-cnt .huawei-cookie-close").on("click",function(){cookieTips()
});
$(".convergent-cookie-agree").on("click",function(){setJPCookie("huawei_store_accept_cookie_flag",true,360);
setJPCookie("huawei_store_accept_cookie_choose","1|1|1",360);
JPCookieBanner()
});
$(".convergent-cookie-close").on("click",function(){if($(".convergent-cookie-agree").length>0){JPCookieBanner()
}else{setJPCookie("huawei_store_accept_cookie_flag",true,360);
setJPCookie("huawei_store_accept_cookie_choose","1|1|1",360);
JPCookieBanner()
}});
$(".second-mask-wrap").on("click",function(){$(".second-navigation .second-nav .icon-app").click()
})
});
var lastWinWidth=$(window).width();
$(window).on("resize",function(){if($(".huawei-convergent-cookie").length>0){var a=$(window).width();
if(a!=lastWinWidth){showJpCookie();
lastWinWidth=a
}}else{showCookieTip()
}});
var site=window.digitalData.page.pageInfo.siteCode2.toUpperCase();
var pre_url=supportv2.supportApiUrl+"/services/service/";
function getSiteLanguage(){return window.digitalData.page.pageInfo.language?window.digitalData.page.pageInfo.language.replace("_","-"):""
}function setHotKeysList(){var a=$("#search-result .hot_word-v3 ul");
a.empty();
var c="";
var b={};
if(typeof sgwHost=="undefined"||sgwHost==null||sgwHost==""){c=pre_url+"vofficial/hot";
b={qAppName:"HuaweiOfficial",site:site,language:getSiteLanguage()}
}else{c=sgwHost+"/cmkt/venus/hot/1";
b={appName:"HuaweiOfficial",language:window.digitalData.page.pageInfo.siteCode2.toUpperCase()}
}if(checkStorageStatus()){if(window.sessionStorage[digitalData.page.pageInfo.siteCode+"_hotkeyList"]){var h=JSON.parse(window.sessionStorage[digitalData.page.pageInfo.siteCode+"_hotkeyList"]);
for(var d=0,g=h;
d<g.length;
d++){if(d==5){break
}if(window.location.href.indexOf("/support")>0){var f=" <li><a><i class='icon_search'></i><span>"+g[d].key+"</span></a></li>"
}else{var f=" <li><a><i class='icon_search'></i><span>"+g[d].key+"</span></a></li>"
}a.append(f)
}return false
}getHotKeysList(c,b,1,a)
}else{getHotKeysList(c,b,0,a)
}}function getHotKeysList(c,b,a,d){if(typeof sgwHost=="undefined"||sgwHost==null||sgwHost==""){$.ajax({url:c,type:"GET",data:b,dataType:"jsonp",jsonp:"jsonp",success:function(h){if(h.length>0&&h!=null){if(a==1){window.sessionStorage[digitalData.page.pageInfo.siteCode+"_hotkeyList"]=JSON.stringify(h)
}for(var f=0;
f<h.length;
f++){if(f==5){break
}if(window.location.href.indexOf("/support")>0){var g=" <li><a><i class='icon_search'></i><span>"+h[f].key+"</span></a></li>"
}else{var g=" <li><a><i class='icon_search'></i><span>"+h[f].key+"</span></a></li>"
}d.append(g)
}}}})
}else{$.ajax({url:c,type:"GET",data:b,dataType:"json",beforeSend:function(f){f.setRequestHeader("SGW-APP-ID",sgwAppId)
},success:function(j){if(j!=null&&j.result!=null&&j.result.length>0){if(a==1){window.sessionStorage[digitalData.page.pageInfo.siteCode+"_hotkeyList"]=JSON.stringify(j.result)
}for(var g=0;
g<j.result.length;
g++){if(g==5){break
}var f=j.result;
if(window.location.href.indexOf("/support")>0){var h=" <li><a><i class='icon_search'></i><span>"+f[g].key+"</span></a></li>"
}else{var h=" <li><a><i class='icon_search'></i><span>"+f[g].key+"</span></a></li>"
}d.append(h)
}}}})
}}function showAssociatedproducts(f){var b=Mkt.Util.trim(f.val());
if(b.length<2){f.siblings("i.arrow").find(".icon_public").addClass("icon_disabled");
if(b==""){$("#search_area .suggested_result").hide();
$("#search_area .hot_word").show();
return
}}else{f.siblings("i.arrow").find(".icon_public").removeClass("icon_disabled")
}$(".associated_list").scrollTop(0);
var a=$(".associated_list").empty();
var d=window.location.href.split("/"+digitalData.page.pageInfo.siteCode2+"/")[0];
if(d==window.location.href){d=window.location.href.split("/"+digitalData.page.pageInfo.siteCode2+".htm")[0]
}var c=d+"/"+digitalData.page.pageInfo.siteCode2+"/_jcr_content.allProducts.json";
if(checkStorageStatus()){if(!sessionStorage[digitalData.page.pageInfo.siteCode+"_all"]){$.getJSON(c,function(g){sessionStorage[digitalData.page.pageInfo.siteCode+"_all"]=g.allProduct;
setAssociatedProducts(b,g.allProduct.split(","),a)
})
}else{setAssociatedProducts(b,sessionStorage[digitalData.page.pageInfo.siteCode+"_all"].split(","),a)
}}else{$.getJSON(c,function(g){setAssociatedProducts(b,g.allProduct.split(","),a)
})
}}function setAssociatedProducts(d,g,j){var f=$("#all_search_url").attr("href");
$(".suggested_result,.hot_word").hide();
if(d.length>0){var a=parseInt($(".suggested_result").attr("search_num")-1);
var b=0;
for(var c=0;
c<g.length;
c++){var h=HeightKey(g[c],d,"strong");
if(h!=g[c]){b++;
if(window.location.href.indexOf("/support")>0){j.append("<li class='associated_key'><a href='"+f+"?keyword="+encodeURIComponent(g[c])+"&tag=support'><i class='icon_search'></i><span>"+h+"</span></a></li>")
}else{j.append("<li class='associated_key'><a href='"+f+"?keyword="+encodeURIComponent(g[c])+"'><i class='icon_search'></i><span>"+h+"</span></a></li>")
}$(".hot_word").hide();
$(".suggested_result").show();
if(b>a){break
}}}j.find("li a").each(function(i){$(this).on("click",function(){analyticsSubmit("Site Search",g[i],"Autosuggest",EVENT_AUTO_SUGGEST_SEARCH)
})
});
$("li.associated_key").eq(0).addClass("default-pro");
$("li.associated_key").length==0?$(".suggested_result").hide():""
}else{$(".suggested_result").hide()
}}function cookieTips(){var a=$(window).width();
$(".huawei-bootom-cookie").hide();
setCookie("agreed-huawei-cookiepolicy","1");
$("#footer-v3").removeAttr("style");
$(".custom-service").removeAttr("style");
$(".supportquestionnairedom-side").removeAttr("style");
$(".manhattan_topBtn").removeAttr("style");
$("#content-v3-compare").css({transform:"none","-webkit-transform":"none"});
$("#up").css("bottom",5+"vh");
$(".post-create").removeAttr("style");
$(".cbg-backtotop").css("bottom",50+"px");
$(".emui9-backtotop").css("bottom",50+"px");
$("body").removeClass("hasCookie");
if(a<1024){$(".custom-service-container,.scroll-top").removeAttr("style");
$("#livechat-compact-container").css("z-index",2147483639);
$(".header-gblnav-default").css("bottom","0px");
$(".huawei-bootom-cookie").hide(function(){if($(".app-nav-icon").hasClass("clicked")){var f=$(window).height()-$(".app-nav").height()-$(".huawei-bootom-cookie:visible").outerHeight(),d=$(".second-navigation:visible").height(),c=$(".app-nav").height();
$(".header-wrap").height(f+d-$(".header-gblnav-default").height());
$("#header-v3").css({height:f+d,top:c-d+"px","z-index":151})
}else{headerHeigh()
}}).css("height","0")
}var b=$(".content-v3-compare");
if(b.is(":visible")){b.css({top:"100%"})
}if($(".support-bootom-cookie").length>0){$(".support-bootom-cookie").css("bottom",0)
}}$(document).on("click",".convergent-cookie-close,.convergent-cookie-button a",function(){if($(".support-bootom-cookie").length>0){$(".support-bootom-cookie").css("bottom",0)
}});
function showCookieTip(g){if(window.integrationJsInterface||window.integrationJsInterfaceWebview){return
}if($(".huawei-convergent-cookie").length>0){return
}if($("#cookie-type").val()=="othercookie"){delCookie("agreed-huawei-cookiepolicy");
headerHeigh();
return
}var f=getCookie("agreed-huawei-cookiepolicy");
if(f=="1"){$(".huawei-bootom-cookie").remove();
headerHeigh();
$("body").removeClass("hasCookie")
}else{$(".huawei-bootom-cookie").show();
var c=$(window).width();
var d=$(".huawei-bootom-cookie").outerHeight();
if($(".huawei-bootom-cookie").hasClass("cookie-style-two")){d=$(".huawei-cookie-cnt").outerHeight()
}$("#footer-v3").css("padding-bottom",d+"px");
$(".manhattan_topBtn").css("bottom",d+10+"px");
$(".emui9-backtotop").css("bottom",d+10+"px");
$(".manhattan_topBtn").css("bottom",d+10+"px");
$(".post-create").css({bottom:d+10+"px",top:"auto"});
$(".cbg-backtotop").css("bottom",d+15+"px");
$("body").addClass("hasCookie");
if(c<1024){$(".header-gblnav-default").css("bottom",d+"px");
$(".custom-service-container,.scroll-top").css("z-index",207)
}else{if($(".custom-service").length>0&&IsPersonalComputer()){$(".custom-service").css("bottom",d+22+"px");
var b=$(".custom-service").css("bottom");
var a=$(".custom-service").outerHeight();
$(".supportquestionnairedom-side").css("bottom",parseInt(b?b:0)+parseInt(a?a:0)+"px")
}}}}function JPCookieBanner(){var a=$(window).width();
$(".huawei-convergent-cookie").hide();
$(".custom-service").removeAttr("style");
$(".supportquestionnairedom-side").removeAttr("style");
$(".manhattan_topBtn").removeAttr("style");
$("#content-v3-compare").css({transform:"none","-webkit-transform":"none"});
$("#up").css("bottom",5+"vh");
$(".post-create").removeAttr("style");
$(".cbg-backtotop").css("bottom",50+"px");
$(".emui9-backtotop").css("bottom",50+"px");
$("body").removeClass("convergentCookie");
if(a<1024){$(".custom-service-container,.scroll-top").removeAttr("style");
$("#livechat-compact-container").css("z-index",2147483639);
$(".header-gblnav-default").css("bottom","0px")
}var b=$(".content-v3-compare");
if(b.is(":visible")){b.css({top:"100%"})
}}function setJPCookie(d,g,b){var a=b*24*60*60*1000;
var c=new Date(+new Date()+a);
var f=window.siteCode;
document.cookie=d+"="+g+";expires="+c.toUTCString()+";domain=huawei.com;path=/"+f+";"
}function showJpCookie(){if(window.integrationJsInterface||window.integrationJsInterfaceWebview){return
}var f=getCookie("huawei_store_accept_cookie_flag");
if(!f||f=="false"){$(".huawei-convergent-cookie").show();
var c=$(window).width();
var d=$(".huawei-convergent-cookie").outerHeight();
$(".manhattan_topBtn").css("bottom",d+10+"px");
$(".emui9-backtotop").css("bottom",d+10+"px");
$(".post-create").css({bottom:d+10+"px",top:"auto"});
$(".cbg-backtotop").css("bottom",d+15+"px");
$("body").addClass("convergentCookie");
if(c<1024){$(".header-gblnav-default").css("bottom",d+"px");
$(".custom-service-container,.scroll-top").css("z-index",207)
}else{if($(".custom-service").length>0&&IsPersonalComputer()){$(".custom-service").css("bottom",d+22+"px");
var b=$(".custom-service").css("bottom");
var a=$(".custom-service").outerHeight();
$(".supportquestionnairedom-side").css("bottom",parseInt(b?b:0)+parseInt(a?a:0)+"px")
}}}}function headerHeigh(){if($(".product-detail-container").not("#More_Support").length>0){$("body").addClass("v3-suppro-detail")
}}function setSessionuuid(d,b,a,c){$.ajax({type:"GET",async:false,url:deleteHttp(d),dataType:"jsonp",jsonp:"jsonp",data:{},success:function(f){a.val(f.sessionuuid);
c.attr("src",b+"?tm="+Math.random()+"&sessionuuid="+f.sessionuuid+"&timep="+Date().valueOf())
}})
}function IEVersion(){var h=navigator.userAgent;
var d=h.indexOf("compatible")>-1&&h.indexOf("MSIE")>-1;
var g=h.indexOf("Edge")>-1&&!d;
var i=h.indexOf("Trident")>-1&&h.indexOf("rv:11.0")>-1;
var c=h.indexOf("HUAWEIALP")>-1||h.indexOf("HUAWEISHT")>-1||h.indexOf("HUAWEICMR")>-1;
var a=0;
if(d){var b=new RegExp("MSIE (\\d+\\.\\d+);");
b.test(h);
var f=parseFloat(RegExp["$1"]);
if(f==7){a=1
}else{if(f==8){a=1
}else{if(f==9){a=1
}else{if(f==10){a=1
}else{a=1
}}}}}else{if(g){a=-1
}else{if(i){a=-1
}else{if(c){a=1
}}}}if(a==1){$(".huawei-ie-tips").slideDown(500)
}else{$(".huawei-ie-tips").remove()
}}function cookieBListenClick(){$("a,button").not(".convergent-cookie-agree").on("click",function(){setJPCookie("huawei_store_accept_cookie_flag",true,360);
if(ctlAnalysisCookie){activeCookieScripts("analysis-cookie")
}if(ctlAdvertiseCookie){activeCookieScripts("advertise-cookie")
}})
}function appEmbedded(){if(window.integrationJsInterface||window.integrationJsInterfaceWebview){$("body").addClass("app-hidden")
}}var defaultImgLogo=$(window).width()<1024?"/etc/designs/huawei-cbg-site/clientlib-v3/images/loading-40.png":"/etc/designs/huawei-cbg-site/clientlib-v3/images/loading-80.png";
var buyFeature=function(g,A,H,j){var m=g||$(this);
var D=m.attr("data-buybtntype");
var C=m.attr("data-pid");
var q=m.attr("data-pname");
var F=m.attr("data-targettype");
var l=m.attr("data-eventtype");
var I=m.attr("data-position");
var f=window.digitalData.page.pageInfo.siteCode2;
if(m.hasClass("eCommerce-buy")){var c=m.data("ecbuylink"),y=m.attr("data-ecpid"),v=m.data("ecopeninnewpage"),G=m.attr("data-btnlinkinfo"),k=m.attr("data-buttonType");
var b=v?"_blank":"_self";
var p=window.integrationJsInterface||window.integrationJsInterfaceWebview;
if(p){p.startAppActivity(y);
return
}if(k==="explore"&&G){buyToPdp_gtm(j,I,l);
fun_ecommerce(b,G)
}else{buyToThirdParty_gtm(j,I,l,m);
fun_ecommerce(b,c)
}return
}if(D=="none"){buyToPdp_gtm(j,I,l);
var c=m.attr("data-btnlinkinfo");
if(c.indexOf("/content/huawei-cbg-site")==0){c=c.replace("/content/huawei-cbg-site","")
}if(F=="_self"){window.location.href=c
}else{window.open(c)
}}else{if(D=="partner"){buyOpenPopup_gtm(j,I,l);
var B=m.attr("data-pcountrybeal")=="true";
var u=m.attr("data-pcountrytitle");
u=!!u?u:Mkt.I18n.get("Select Country");
createPopupToBuy();
var r=A&&A.showStoreFinder;
var d="_self";
var x="";
if(r){d=A.openStoreFinderInNewPage?"_blank ":"_self";
x=A.storeFinderLink
}var J=m.attr("data-btnlinkinfo");
if(J.indexOf(".html")>0){J=J.substring(0,J.lastIndexOf(".html"))
}var o=J+"/_jcr_content.partners-v4.json";
var h={};
h.showStoreFinder=r;
h.storeFinderLink=x;
h.storeFinderInNewPage=d;
h.pCountryBeal=B;
h.pCountryTitle=u;
var i={};
i.nameforga=j;
i.eventtype=l;
i.bannerposition=I;
i.targetType=F;
fun_partner(o,h,i,H)
}else{if(D=="third-party-site"){var n=false;
var c=m.attr("data-btnlinkinfo")||"";
if(c){var a=c.indexOf(window.location.href)!=-1;
var z=Mkt.Util.isDispatcher?"/":"/content/huawei-cbg-site/";
var t=c.indexOf(window.location.origin+z+f)!=-1;
var E=Mkt.Util.isDispatcher?c.lastIndexOf("/select")!=-1:c.indexOf("/select.html")!=-1;
var w=m.attr("data-pagetype");
if(t&&E){n=true
}else{if(a&&c.indexOf("#")!=-1){l="product-detail-footer"
}else{if(w&&w=="search"&&c.indexOf("#")!=-1){l="search-product-detail-footer"
}}}}buyToThirdParty_gtm(j,I,l,m,n);
fun_thirdParty(F,c,f)
}else{if(D=="global-buy"){buyOpenPopup_gtm(j,I,l);
if(!!C){createPopupToBuy();
var i={};
i.nameforga=j;
i.eventtype=l;
i.bannerposition=I;
i.targetType=F;
getECSiteList(f,C,q,i);
if($.isIos()){$("#pdbuypage").trigger("click")
}}}else{console.log(C+"-->"+D)
}}}}};
var fun_partner=function(c,l,d,k){var p=l.showStoreFinder;
var b=l.storeFinderLink;
var j=l.storeFinderInNewPage;
var m=l.pCountryBeal;
var g=l.pCountryTitle;
var f=d.nameforga;
var n=d.eventtype;
var i=d.bannerposition;
var a=d.targetType;
$.getJSON(c,function(r){var v="";
if(m){v="pdbuypage-pcountry";
$("#pdbuypage .pcountry-selbox").show();
$("#pdbuypage .pcountry-countryname").html(g);
if(r&&r.countries){var u="";
for(var q in r.countries){u+='<li class="pcountry-list-li" value="'+q+'" title="'+r.countries[q]+'">'+r.countries[q]+"</li>"
}$("#pdbuypage .pcountry-list").append(u)
}h()
}if(r&&r.partners){var t="";
r.partners.forEach(function(x,w,y){t+='<li class="pdbuypage-listitem pdbuypage-listitem-partner '+v+'" data-pcountry="'+x.countryTag+'"><a href="'+x.link+'" data-selectedpartnerbuy="'+x.name+'" data-nameforga="'+f+'" data-eventtype="'+n+'" data-bannerposition="'+i+'"  target="'+a+'" data-parterlink="'+x.link+'" class="pdbuypage-listitem-link"><img src="'+x.icon+'" onerror="javascript:this.src=\''+defaultImgLogo+'\'" alt="'+x.name+'" class="pdbuypage-listitem-img" /></a></li>'
});
$("#pdbuypage .pdbuypage-listul").html(t);
$("#pdbuypage .pdbuypage-title-tipinfo").html(Mkt.I18n.get("Your Huawei device is available here"))
}if(!!p){$(".pdbuypage-footinfo").show();
$(".pdbuypage-footinfo span").html(Mkt.I18n.get("If you want to buy in store, please click"));
$(".pdbuypage-footinfo a").text(" "+Mkt.I18n.get("Store finder")).attr({href:b,target:j})
}else{$(".pdbuypage-footinfo").hide()
}if(k&&k.length>0){$(".pdbuypage-disclaimer").html(k).show()
}o()
});
function h(){$(".pcountry-active").on("click",function(){var q=$(this);
if(q.attr("type")=="hide"){q.attr("type","show");
q.find(".pcountry-arrow").addClass("pcountry-arrowup");
q.parent().find(".pcountry-list").slideDown(300);
if($(window).width()<1024){$(".pcountry-bg").show();
$(".pdbuypage-listul").css("overflow-y","hidden")
}}else{q.attr("type","hide");
q.find(".pcountry-arrow").removeClass("pcountry-arrowup");
q.parent().find(".pcountry-list").slideUp(300);
$(".pcountry-bg").hide();
$(".pdbuypage-listul").css("overflow-y","auto")
}});
$(".pcountry-list-li").on("click",function(){$(".pcountry-list-liactive").removeClass("pcountry-list-liactive");
$(".pdbuypage-listitem-partner").hide();
var t=$(this);
t.addClass("pcountry-list-liactive");
var r=t.text();
var q=t.attr("value");
$(".pcountry-active .pcountry-countryname").text(r).attr("title",r);
$(".pcountry-active").attr({value:q,type:"hide"});
$(".pcountry-arrow").removeClass("pcountry-arrowup");
$(".pcountry-list").slideUp(300,function(){$(".pcountry-bg").hide();
$(".pdbuypage-listul").css("overflow-y","auto")
});
$(".pdbuypage-listitem-partner").each(function(w,u){var v=$(u);
if(v.attr("data-pcountry")==q){v.show().css("float","left")
}else{v.hide()
}})
});
$(".pcountry-bg").on("click",function(){$(".pcountry-list").slideUp(300,function(){$(".pcountry-bg").hide();
$(".pdbuypage-listul").css("overflow-y","auto");
$(".pcountry-active").attr({type:"hide"});
$(".pcountry-arrow").removeClass("pcountry-arrowup")
})
})
}function o(){var q=0;
if($(window).width()>=1024){if($(".pdbuypage-listul .pdbuypage-listitem").length>3){$(".pdbuypage-listul .pdbuypage-listitem").css("float","left")
}if($.isIos()){q=$(window).scrollTop();
$("html").addClass("htmlbody_scroll")
}}else{if($(".pdbuypage-listul .pdbuypage-listitem").length>2){$(".pdbuypage-listul .pdbuypage-listitem").css("float","left")
}q=$(window).scrollTop();
$("html").addClass("htmlbody_scroll")
}$("body.huawei-v4").css("overflow-y","hidden");
$("#pdbuypage").stop().slideDown(300,function(){setTimeout(function(){$("#pdbuypage").trigger("click")
},200);
setListHeight()
});
$(".pdbuypage-close").on("click",function(){$("#pdbuypage").slideUp(300,function(){$("body.huawei-v4").css("overflow-y","auto");
$("html").removeClass("htmlbody_scroll");
if($(window).width()<1024||$.isIos()){$(window).scrollTop(q)
}$("#pdbuypage").remove()
})
})
}};
var fun_thirdParty=function(c,d,b){if(d.indexOf("http")=="-1"){var a=window.location.href.split("/"+b+"/")[0];
if(d.indexOf("/")==0){d=a+d
}else{d=a+"/"+d
}}else{d=d
}if(c=="_self"){window.location.href=d
}else{window.open(d)
}};
var getECSiteList=function(g,c,f,b){var d=[];
var a="/content/dam/huawei-cbg-site/en/worldwide/js/ecommerce-site-list.json";
$.ajax({url:a,type:"GET",success:function(h){if(h&&h.selfEcommerce){h.selfEcommerce.forEach(function(i){d.push(i.siteCode)
})
}},complete:function(){fun_globalBuy(g,c,f,b,d)
}})
};
var arrSortBySiteNameLetter=function(a,b){return a.sort(function(d,c){return d[b].localeCompare(c[b])
})
};
var areaSiteSort=function(b,c){var a=[],d=[];
for(var f in b){if(Object.prototype.hasOwnProperty.call(b,f)){b[f].countryName=f;
if(c.length>0&&c.indexOf(f)>-1){b[f].isECSite="true";
a.push(b[f])
}else{b[f].isECSite="false";
d.push(b[f])
}}}a=arrSortBySiteNameLetter(a,"siteName");
d=arrSortBySiteNameLetter(d,"siteName");
return a.concat(d)
};
var fun_globalBuy=function(h,g,n,d,c){var f=d.nameforga;
var m=d.eventtype;
var i=d.bannerposition;
var a=d.targetType;
var o=location.href.split("/"+h+"/")[0];
if(o.indexOf(".html")>-1){o=location.href.split("/"+h+".html")[0]
}var k=o+"/en/hidden/product/"+g+"/_jcr_content/content.json";
$.getJSON(k,function(q){if(!q||!q.buyInfo){return
}var p=j(q.buyInfo);
$(".pdbuypage-box").addClass("pdbuypage-box-global");
$(".pdbuypage-title-productname").html(n).parent().show();
$(".pdbuypage-title-productplane").html(Mkt.I18n.get("Region to buy"));
$(".pdbuypage-title-tipinfo").html(Mkt.I18n.get("Please Select Your Country"));
$(".pdbuypage-listul").html(p);
$(".pdbuypage-footinfo").hide();
globalBuyPopUpWindowUX()
});
var j=function(u){var r=JSON.parse(u);
var q="";
for(var v in r){if(Object.prototype.hasOwnProperty.call(r,v)){var t=areaSiteSort(r[v],c);
var p=b(t);
if(v==="Middle East / Africa"){v="Africa and Middle East";
q=l(v,p)+q
}else{q+=l(v,p)
}}}return q
};
var l=function(q,p){return'<li class="pdbuypage-listitem pdbuypage-listitem-global"><p class="pdbuypage-listitem-area">'+q+'</p><div class="pdbuypage-listitem-country">'+p+"</div></li>"
};
var b=function(q){var p="";
for(var r in q){if(Object.prototype.hasOwnProperty.call(q,r)){p+='<a href="'+q[r].buyLink;
p+='" data-selectedglobalbuy="'+q[r].countryName;
p+='" data-nameforga="'+f;
p+='" data-eventtype="'+m;
p+='" data-bannerposition="'+i;
p+='" target="'+a;
p+='" data-parterlink="" class="pdbuypage-listitem-link">';
p+='<span class="pdbuypage-listitem-name">'+q[r].localSiteName+"</span>";
if(q[r].isECSite==="true"){p+='<span class="icon icon-cart"></span>'
}p+="</a>"
}}return p
}
};
var setListHeight=function(){var a=$(".pdbuypage-box").height();
var d=$(".pdbuypage-title").is(":visible")?$(".pdbuypage-title").outerHeight(true):0;
var f=$(".pcountry-selbox").is(":visible")?$(".pcountry-selbox").outerHeight(true):0;
var c=$(".pdbuypage-footinfo").is(":visible")?$(".pdbuypage-footinfo").outerHeight(true):0;
var b=$(".pdbuypage-disclaimer").is(":visible")?$(".pdbuypage-disclaimer").outerHeight(true):0;
$(".pdbuypage-list").height(a-d-f-c-b)
};
var globalBuyPopUpWindowUX=function(){var b=0;
if($(window).width()<1024){b=$(window).scrollTop();
$("html").addClass("htmlbody_scroll")
}else{if($.isIos()){b=$(window).scrollTop();
$("html").addClass("htmlbody_scroll")
}}var a=$(window).scrollTop();
$("body").css({overflow:"hidden",position:"fixed",top:-a,width:"100%"});
$("#pdbuypage").stop().slideDown(300,function(){setTimeout(function(){$("#pdbuypage").trigger("click")
},200);
setListHeight()
});
$(".pdbuypage-close").on("click",function(){$("body").css({overflow:"auto",position:"static",top:"auto",width:"auto"});
$("html").removeClass("htmlbody_scroll");
$(window).scrollTop(a);
$("#pdbuypage").slideUp(300,function(){$("#pdbuypage").remove()
})
});
$(".pdbuypage-listitem-global .pdbuypage-listitem-area").click(function(){$(this).parent().toggleClass("active");
$(this).siblings(".pdbuypage-listitem-country").slideToggle()
})
};
var fun_ecommerce=function(a,b){if(b){if(!b.startsWith("http")&&!b.startsWith("https")){if(b.indexOf(".html")==-1){b+=".html"
}if(b.indexOf("/content/huawei-cbg-site")>-1){b=b.split("/content/huawei-cbg-site")[1]
}b=dialogLinkHandler(b)
}if(a==="_self"){window.location.href=b
}else{window.open(b)
}}};
var createPopupToBuy=function(b){var c='<div id="pdbuypage"><div class="pdbuypage-bg"></div><div class="pdbuypage-box"><p class="pdbuypage-close"><svg width="32" height="32" xmlns="http://www.w3.org/2000/svg"><g fill="#3C3C3C" fill-rule="evenodd"><path d="M8 7l17 17-1 1L7 8z"></path><path d="M7 24L24 7l1 1L8 25z"></path></g></svg></p><div class="pdbuypage-title"><p class="pdbuypage-title-product"><span class="pdbuypage-title-productplane"></span><span class="pdbuypage-title-productname"></span></p><p class="pdbuypage-title-tipinfo"></p><p class="pdbuypage-ecommerce-tipinfo"><span class="icon icon-cart"></span><span class="ec-tip-content"> This icon represents that Huawei e-commerce is available in this country or region.</span></p></div><div class="pcountry-selbox" style="display:none"><div class="pcountry-bg"></div><div class="pcountry-country"><p class="pcountry-active" type="hide"><b class="pcountry-countryname"></b><b class="pcountry-arrow"></b></p><ul class="pcountry-list"></ul></div></div><div class="pdbuypage-list"><ul class="pdbuypage-listul"></ul></div><p class="pdbuypage-footinfo"><span></span><a href="javascript:;" class="pdbuypage-shopSearch"></a></p><p class="pdbuypage-disclaimer"></p></div></div>';
var a=b||".huawei-v4";
if($(a+" .pdbuypage").length>0){$(a+" .pdbuypage").remove()
}$(a).append(c);
$("#pdbuypage").on("click",function(){$("#pdbuypage").css("z-index",parseInt($("#pdbuypage").css("z-index"))+1)
})
};
var buyBtnAttributes=function(f,c,b,d){if(!f){return
}if(f.buyButtonMode&&f.buyButtonMode.buyButtonText&&f.buyButtonMode.buyButtonText.length>0){f.buyButtonText=f.buyButtonMode.buyButtonText
}else{f.buyButtonText=Mkt.I18n.get("Buy")
}var a={};
a["data-pid"]=f.productId;
a["data-pname"]=f.marketingName;
if(f.buyButtonMode){a["data-buybtntype"]=f.buyButtonMode.buttonType;
a["data-targettype"]=f.buyButtonMode.openInNewPage?"_blank":"_self";
a["data-eventtype"]=d;
a["data-position"]=b;
switch(a["data-buybtntype"]){case"none":f.buyButtonText=Mkt.I18n.get("Explore Product");
a["data-btnlinkinfo"]=f.detailLink;
break;
case"partner":a["data-storelink"]=f.buyButtonMode.storeFinderLink;
a["data-btnlinkinfo"]=f.detailLink;
a["data-pcountrybeal"]=f.buyButtonMode.partnerCountryFilterEffective;
a["data-pcountrytitle"]=f.buyButtonMode.partnerCountryFilterTitle;
break;
case"third-party-site":a["data-btnlinkinfo"]=$(window.width)<1024?f.buyButtonMode.mobileThirdPartySiteLink:f.buyButtonMode.thirdPartySiteLink;
break;
case"global-buy":a["data-btnlinkinfo"]=f.detailLink;
break;
default:break
}}a["data-enableec"]=f.enableEc;
a["data-ecpid"]=f.ecProductId;
a["data-ecbuylink"]=f.ecBuyLink;
a["data-ecopeninnewpage"]=f.ecOpenInNewPage;
a["data-onepricedisplay"]=f.onePriceDisplay;
f.buyButtonAttr=a
};
var getMinPriceAndInv=function(c,a){var b=$.Deferred();
var d={};
d.api="queryMinPriceAndInv";
d.type="GET";
d.data={};
d.data.productIds=c;
if(a!=undefined){d.async=a
}d.success=function(f){b.resolve(f)
};
d.error=function(h,f,g){b.reject(h,f,g)
};
if(a!=undefined&&!a){return ecCom.ajaxReq(d)
}else{ecCom.ajaxReq(d);
return b.promise()
}};
var getPrdDisplayDetailInfo=function(a,b){var c=$.Deferred();
var d={};
d.api="queryPrdDisplayDetailInfo";
d.type="GET";
d.data={};
d.data.productId=a;
if(b!=undefined){d.async=b
}d.success=function(f){c.resolve(f)
};
d.error=function(h,f,g){c.reject(h,f,g)
};
if(b!=undefined&&!b){return ecCom.ajaxReq(d)
}else{ecCom.ajaxReq(d);
return c.promise()
}};
var getSbomByCodes=function(d,a){var b=$.Deferred();
var c={};
c.api="querySbomByCodes";
c.type="GET";
c.data={};
c.data.sbomCodes=d;
if(a!=undefined){c.async=a
}c.success=function(f){b.resolve(f)
};
c.error=function(h,f,g){b.reject(h,f,g)
};
if(a!=undefined&&!a){return ecCom.ajaxReq(c)
}else{ecCom.ajaxReq(c);
return b.promise()
}};
var ecRenderEcomercePrice=function(){var c=[];
var b=ecCom.I18n.get("ec_buy");
function f(j){var k=$.map(j,function(n,l){var m=$(n).find(".global-buy-button").hide();
var o=m.attr("data-ecpid")||"";
if(m.attr("data-enableec")=="true"&&o!=""){m.addClass("eCommerce-buy")
}return o
});
return k
}function h(j){return j.filter(function(l,k,m){return m.indexOf(l,0)===k
})
}c=c.concat(f($(".hero-carousel__slide-wrap")));
c=c.concat(f($(".products-card-component .product-card")));
c=c.concat(f($(".product-carousel-component .product-carousel__product")));
c=h(c);
if(c.length==0){return
}getMinPriceAndInv(c).then(function(k){var j=new Map();
if(k.data.minPriceAndInvList){$.each(k.data.minPriceAndInvList,function(m,l){j.set(l.productId+"",l)
})
}d(j);
a(j);
g(j)
},function(){var j=new Map();
d(j);
a(j);
g(j)
});
function d(j){var k=$(".hero-carousel__slide-wrap");
$.each(k,function(n,m){var l=j.get($(m).find(".global-buy-button").attr("data-ecpid")+"");
if(l&&l.hasInv){$(m).find(".global-buy-button").text(b).show()
}else{$(m).find(".global-buy-button").hide()
}})
}function a(j){var k=$(".products-card-component .product-card");
$.each(k,function(m,l){var o=j.get($(l).find(".global-buy-button").attr("data-ecpid")+"");
if(o){var n=JSON.parse($(l).find('[name="buyBtnInfo"]').val());
if(o.hasInv){var p=i(o,n);
$(l).find(".product-card__price").addClass("has-price-info").html(p);
$(l).find(".global-buy-button").text(b).show()
}else{$(l).find(".global-buy-button").hide()
}}else{$(l).find(".global-buy-button").hide()
}})
}function g(k){var j=$(".product-carousel-component .product-carousel__product");
$.each(j,function(m,l){var o=k.get($(l).find(".global-buy-button").attr("data-ecpid")+"");
if(o){var n=JSON.parse($(l).find('[name="buyBtnInfo"]').val());
if(o.hasInv){var p=i(o,n);
$(l).find(".product-carousel__price").html(p);
$(l).find(".global-buy-button").text(b).show()
}else{$(l).find(".global-buy-button").hide()
}}else{$(l).find(".global-buy-button").hide()
}})
}function i(t,l){var v="";
var o="";
if(showFrom&&!l.onePriceDisplay){if(putFromFront){o=ecCom.I18n.get("ec_from")+" "
}else{v=" "+ecCom.I18n.get("ec_from")
}}var m="";
var k="";
if(t.installmentInfos){m="has-installment";
if(enableInstallmentCfg){k=window.ecInstallmentFullText(t.installmentInfos)
}else{var n=t.installmentInfos.sort(function(x,w){return w.num-x.num
})[0].num;
if(site==="UK"||site==="DE"||site==="ES"){k=ecCom.I18n.get("ec_installment_or")+" "+ecCom.I18n.get("ec_finance_available")
}else{k=ecCom.I18n.get("ec_installment_or")+" "+ecCom.I18n.get("ec_payment_in_installments",[n])
}}}var j=ecCurrency(t.minUnitPrice);
var r=ecCurrency(t.minOrderPrice);
var u=t.minUnitPrice==t.minOrderPrice?"":r;
var q="";
var p="";
if(enableRRP&&u){p="<span>"+RRPText+"</span>"
}if(window.innerWidth>1199.98){q='<div class="ec-price"><span class="from-front">'+o+'</span><p class="sale-price">'+j+'<span class="from-behind">'+v+"</span></p>"+p+(u?'<span class="original-price">'+u+"</span>":"")+'<span class="installment '+m+'">'+k+"</span></div>"
}else{q='<div class="ec-price"><p class="sale-price"><span class="from-front">'+o+"</span>"+j+'<span class="from-behind">'+v+"</span>"+p+'<span class="original-price">'+u+'</span></p><span class="installment '+m+'">'+k+"</span></div>"
}return q
}};
var ecEnableEcommerceLogic=function(){var a=$(".series-list-component,.model-list-component,.psp-list-component,.product-selling-point-component").find(".global-buy-button");
a.each(function(){if($(this).attr("data-enableec")=="true"){$(this).addClass("eCommerce-buy")
}})
};
var currentPageMinPriceAndInvMap=new Map();
var currentPageMinPriceAndInvMapFun=function(){var d=[];
var b;
$(".global-eCommerce-price[data-interfacename='queryMinPriceAndInv']").each(function(){b=$(this).attr("data-ecproductid");
if(b!=null){b=b.trim();
if(""!=b&&d.indexOf(b)==-1){d.push(b)
}}});
if(d.length!=0){var c=getMinPriceAndInv(d,false);
if(c!=null&&c.resultCode===0){var a=c.data.minPriceAndInvList;
if(a){$.each(a,function(f){currentPageMinPriceAndInvMap.set(a[f].productId.toString(),a[f])
})
}}else{console.error(c.message+" : queryMinPriceAndInv")
}}};
$(function(){isECommerceSite!="None"&&ecRenderEcomercePrice();
if(isECommerceSite=="Self-eCommerce"||isECommerceSite=="Fusion-eCommerce"){ecEnableEcommerceLogic();
currentPageMinPriceAndInvMapFun()
}$(document).on("click",".global-buy-button",function(f){f.preventDefault();
var h=($(this).prev("input[name='buyBtnInfo']")||{}).val();
var j=JSON.parse(h);
if(j!=null){var d=$(this).attr("data-position");
var i=$(this).attr("data-eventtype");
var c=$(this).attr("data-nameforga");
var g=i=="navi"?c:(c?c+"_"+j.marketingName:j.marketingName);
buyBtnAttributes(j,c,d,i);
for(var b in j.buyButtonAttr){$(this).attr(b,j.buyButtonAttr[b])
}var a={showStoreFinder:j.showStoreFinder,openStoreFinderInNewPage:j.openStoreFinderInNewPage,storeFinderLink:j.storeFinderLink};
buyFeature($(this),a,j.disclaimer,g)
}})
});
var EVENT_TYPE_EMAIL_SUBMIT_SUCCESS="emailSubSuccess";
var EVENT_TYPE_EMAIL_SUBMIT_FAIL="emailSubFail";
var EVENT_TYPE_SPAREPART_PRICE="supportSparepartPrice";
var EVENT_TYPE_M2M_DISTRIBUTOR="m2mDistributor";
var EVENT_TYPE_CONTACT_US_FEEDBACK="contactUsFeedback";
var EVENT_TYPE_CONTACT_US_HOTLINE="contactUsHotline";
var EVENT_TYPE_CONTACT_US_TECHNICAL="contactUsTechnical";
var EVENT_TYPE_APPOINTMENT_SERVICE="appointmentServiceSuccess";
var EVENT_TYPE_FIND_A_STORE="findAStore";
var EVENT_TYPE_SUPPORT_SEARCH_AND_RESULT="supportSearchAndResultSuccess";
var EVENT_TYPE_PRODUCT_FILTER="headerProductFilter";
var EVENT_TYPE_PRODUCT_COMPARE_ADD="productCompareAdd";
var EVENT_TYPE_PRODUCT_CANCEL_CLOSE="productCancelClose";
var EVENT_TYPE_PRESS_NEWS_LIST="pressNewsList";
var EVENT_TYPE_PRESS_NEWS_LIST_SEARCH="pressNewsListSearch";
var EVENT_TYPE_PRESS_AWARD_LIST="pressAwardList";
var EVENT_TYPE_PRESS_VIDEO_LIST="pressVideoList";
var EVENT_TYPE_PDP_FAQ_SEARCH="supportPdpFaqSearch";
var EVENT_TYPE_FAQ_PDP_FEEDBACK="faqDetailpageIsthisContentHelpful";
var EVENT_TYPE_POST_REPAIR="submitPostalRepairApointment";
var EVENT_TYPE_FIND_SERVICE_CENTER_COUNTRY_CITY="submitFindServiceByCountryCity";
var EVENT_TYPE_FIND_SERVICE_CENTER_DISTANCE="submitFindServiceByAddressDistance";
var EVENT_TYPE_VIDEO_CLOSED="videoClosed";
var EVENT_TYPE_SEARCH_RECYCLING_POINT="searchRecyclingPoint";
var EVENT_TYPE_SP_LANDING_PAGE_SEARCH="supportLandingPageSearch";
var EVENT_AUTO_SUGGEST_SEARCH="autoSuggestSearch";
var EVENT_PURE_SEARCH="pureSearch";
var EVENT_SEARCH_BY_DROPDOWN_FILTER="searchByDropdownFilter";
var EVENT_COMPARISON_FILTER="comparisonFilter";
var EVENT_CLICK_FIND_SERVICE_CENTER="clickOnSupportServiceCenterResult";
var EVENT_TYPE_SHOW_CONTENT="showContent";
var EVENT_TYPE_HIDE_CONTENT="hideContent";
var EVENT_TYPE_HOTSPOTS_CLICK="hotspotsClicked";
var EVENT_TYPE_PS_PRODUCT_LISTING_SEARCH="supportProductListingSearch";
var EVENT_TYPE_SUPPORT_PDP_DROPDOWN="supportPdpDropdown";
var EVENT_TYPE_HOT_SEARCH="HotSearch";
var EVENT_TYPE_SUPPORT_SEARCH="SupportSearch";
var EVENT_TYPE_OPEN_MENU_FIRST_LEVEL="openMenuFirstLevel";
var EVENT_TYPE_OPEN_MENU_SECOND_LEVEL="openMenuSecondLevel";
var EVENT_TYPE_SUPPORT_SEARCH_AUTO_SUGGEST="supportSearchAutoSuggest";
var EVENT_TYPE_NEWS_LIST_LOAD_MORE="newsListLoadMore";
var EVENT_TYPE_PRODUCT_MENU_MODULE_LOAD_MORE="productMenuModuleLoadMore";
var EVENT_TYPE_SEARCH_RECYCLING_STORE_CLICK="searchRecyclingStoreClick";
var EVENT_TYPE_EXPRESS_REPAIRE_SERVICE_MODIFY="expressRepaireServiceModify";
var EVENT_TYPE_EXPRESS_REPAIRE_SERVICE_SUBMIT="expressRepaireServiceSubmit";
var EVENT_TYPE_REPAIR_STATUS_INQUIRY_SUMBIT="repairStatusInquirySumbit";
var EVENT_TYPE_DOOR_TO_DOOR_SERVICE_SUBMIT="doorToDoorServiceSubmit";
var EVENT_TYPE_APPOINTMENT_SERVICE_MODIFY="appointmentServiceModify";
var EVENT_TYPE_APPOINTMENT_SERVICE_SUBMIT="appointmentServiceSubmit";
var EVENT_TYPE_WARRANTY_QUERY_SUBMIT="warrantyQuerySubmit";
var EVENT_TYPE_TOPIC_PAGE_INTERACTIONS="topicPageInteractions";
var EVENT_TYPE_TOPIC_LIST_SITE_SEARCH="topicListSiteSearch";
var EVENT_TYPE_MAIL_SERVICE_SUBMIT="mailServiceSubmit";
var EVENT_TYPE_HOME_PAGE_SITE_SEARCH="homePageSiteSearch";
var EVENT_TYPE_SPAREPARTS_PRICE_SUBMIT="sparePartsPriceSubmit";
var EVENT_TYPE_USER_CENTER_ADD="userCenterAdd";
var EVENT_TYPE_USER_CENTER_MODIFY="userCenterModify";
var EVENT_TYPE_USER_CENTER_DELETE="userCenterDelete";
var pageProductGTMV4=window.digitalData.product?window.digitalData.product.productInfo:"";
function analyticsSubmit(a,b,g,f){if(!a||!b||!g){return
}var h={cat:a,act:b,lab:g,customEventType:f};
for(var d=4;
d<arguments.length;
d++){for(var c in arguments[d]){h[c]=arguments[d][c]
}}DataLayerUtil.addEvent(h);
DataLayerUtil.triggerEvent(f)
}var DataLayerUtil={addEvent:function(a){window.digitalData.event.push({eventInfo:a})
},getEvent:function(c,g){var j=null;
try{if(digitalData&&digitalData.event&&digitalData.event instanceof Array){var b=digitalData.event;
var f=b.length;
for(var a=f-1;
a>=0;
a--){var h=b[a].eventInfo;
if(h.customEventType==c&&h[g]){j=getContent(h[g].toString()).trim();
break
}}}}catch(d){}return j
},triggerEvent:function(a){$(document).trigger(a)
}};
function pushVideoDatalayer(b,c,d,a){window.dataLayer.push(addATCommonFields({event:"video",videoStep:c,videoName:b,productMktName:d?d:"",productCategory:a?a:"",clickName:"video "+b+"_"+c,clickType:"action"}))
}function getCookie(d){var b=d+"=";
var g=decodeURIComponent(document.cookie);
var a=g.split(";");
for(var f=0;
f<a.length;
f++){var h=a[f];
while(h.charAt(0)==" "){h=h.substring(1)
}if(h.indexOf(b)==0){return h.substring(b.length,h.length)
}}return""
}function setCookie(b,g,c){var f=new Date(),a="";
f.setTime(f.getTime()+(c*24*60*60*1000));
a="expires="+f.toUTCString();
document.cookie=b+"="+g+";"+a+";path=/";
return""
}$(document).ready(function(){if($(".contact-us-v2").length>0){function a(f){var d=false;
var c=$(window).height();
var b=f.offset().top;
$(window).on("scroll",function(){var g=$(this).scrollTop();
if(g>b-c-20&&!d){f.find("img.scroll-lazy").each(function(h){$(this).attr("src",$(this).data("src"))
});
d=true
}})
}a($(".contact-us-v2"))
}});