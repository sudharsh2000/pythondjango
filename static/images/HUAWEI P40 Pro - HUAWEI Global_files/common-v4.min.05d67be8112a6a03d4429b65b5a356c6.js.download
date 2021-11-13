(function(){$(function(){var f=$(".mkt-ad-banner");
if(f.length>0){var d=$(".mkt-ad-banner .ad-banner-box ul");
var b={scrollTimer:null,delayTimer:null,height:0,total:0,currentTop:parseInt(d.position().top),timeZone:f.data("timeZone"),speed:f.data("speed")*1000||3000,fontColor:f.data("fontColor")||"#000",bgBeginColor:f.data("bgBeginColor")||"",bgEndColor:f.data("bgEndColor")||"",closeBtnColor:f.data("closeBtnColor")||"#000"};
c();
e();
function c(){$(".mkt-ad-banner,.mkt-ad-banner .ad-item-link").css("color",b.fontColor);
$(".mkt-ad-banner .ad-item-link .icon-arrow").css("borderColor",b.fontColor);
$(".mkt-ad-banner .ad-banner-close .icon-bar").css("backgroundColor",b.closeBtnColor);
if(document.documentMode>0){$(".mkt-ad-banner .ad-banner-close").addClass("isIE")
}if(b.bgBeginColor&&!b.bgEndColor){f.css("background",b.bgBeginColor)
}else{if(!b.bgBeginColor&&b.bgEndColor){f.css("background",b.bgEndColor)
}}if(b.bgBeginColor&&b.bgEndColor){f.removeClass("default-bg")
}}function e(){var h=new Date().getTime();
$.ajax({type:"get",async:false,timeout:30000,url:"/services/server/time/?_="+new Date().getTime(),dataType:"json",success:function(l){h=l.timeStamp
}});
var i=h+(b.timeZone-8)*60*60*1000;
var j=0;
d.children("li").each(function(o){j++;
var n=$(this).data("start");
var m=$(this).data("end");
var p=new Date(n.replace(/-/g,"/")).getTime();
var l=new Date(m.replace(/-/g,"/")).getTime();
if(p>i||l<i){$(this).removeClass("item-valid").addClass("item-invalid")
}});
b.total=d.children("li.item-valid").length;
var k=setTimeout(function(){if(j==d.children("li").length){g();
clearTimeout(k)
}},100)
}function g(){f.delay(600).fadeIn(800);
setTimeout(function(){$(".mkt-ad-banner .ad-content-box.item-valid .ad-content").each(function(i){var j=$(this).height();
b.height=(b.height>j)?b.height:j
});
if(b.height>0){b.height=b.height+16*2;
$(".mkt-ad-banner .ad-banner-box,.mkt-ad-banner .ad-banner-box .ad-content-box").height(b.height)
}},600);
if(b.total>1){var h=1400+3000;
b.delayTimer=setTimeout(function(){b.scrollTimer=setInterval(a,10)
},h);
f.mouseenter(function(){clearInterval(b.scrollTimer);
clearTimeout(b.delayTimer)
});
f.mouseleave(function(){b.delayTimer=setTimeout(function(){b.scrollTimer=setInterval(a,10)
},600)
})
}}$(".mkt-ad-banner .ad-item-link").click(function(){var j=$(this).siblings(".ad-item-txt").text();
var h=$(this).attr("href");
var i={clickName:"banner under navi click "+j+" to "+h,clickType:"navigation",pageCategory:pageCategory,event:"topAdvert",bannerName:"mkt_advertisement_banner_"+j,bannerPosition:"top",pageName:h};
window.dataLayer.push(addATCommonFields(i))
});
$(".mkt-ad-banner .ad-banner-close").click(function(){f.fadeOut(800);
clearInterval(b.scrollTimer);
clearTimeout(b.delayTimer);
var h={clickName:"banner under navi click Close",clickType:"navigation",pageCategory:pageCategory,event:"topAdvert",bannerName:"Close",bannerPosition:"top"};
window.dataLayer.push(addATCommonFields(h))
});
function a(){b.currentTop--;
d.css("top",b.currentTop);
if(b.currentTop==(b.total-1)*-1*b.height){var h=d.children("li.item-valid").first();
d.append(h.clone())
}if(b.currentTop==b.total*-1*b.height){b.currentTop=0;
d.css("top",b.currentTop);
d.children("li.item-valid").last().remove()
}if(b.currentTop%b.height==0){clearInterval(b.scrollTimer);
clearTimeout(b.delayTimer);
b.delayTimer=setTimeout(function(){b.scrollTimer=setInterval(a,10)
},b.speed)
}}}})
}());
window.Mkt=window.Mkt||{};
var sgwHost="";
var sgwAppId="DE1FDF33D6278164A62EC486793F7CCF";
function initSgw(){try{var a=window.digitalData.page.pageInfo.siteCode;
if(a==="cn"){if(typeof mktConfig!=="undefined"&&mktConfig.sgwApi!=""&&mktConfig.sgwApi!=null){sgwHost=mktConfig.sgwApi;
return
}sgwHost="https://sgw-cn.c.huawei.com/forward"
}}catch(b){}}initSgw();
var countryCode=window.digitalData?window.digitalData.page.pageInfo.countryCode:"";
var pageCategory=window.digitalData?window.digitalData.page.category.pageType:"";
var DEFAULT_NAVI="navi";
var DEFAULT_BANNER="banner";
var DEFAULT_SERIES="series";
var DEFAULT_RELATE="relate";
var DEFAULT_PSP_COMPONENT="psp-component";
var DEFAULT_PLP_SERIES="plp-list";
var DEFAULT_PLP_MODEL_LIST="plp-model";
const GA_THIRD_PARTY={navi:{event:"naviPop",clickName:"header navi_click to pop_huawei",clickType:"action",productMktName:"${name}",productPosition:"${position}"},banner:{event:"bannerPop",clickName:"banner click to pop_huawei_${name}",clickType:"action",bannerName:"${name}",bannerPosition:"${position}"},series:{event:"seriesPop",clickName:"series_click to pop_huawei_${position}",clickType:"navigation",productMktName:"${name}",productPosition:"${position}"},relate:{event:"relateProductsPop",clickName:"product list_click to pop_huawei_${position}",clickType:"action",productMktName:"${name}",productPosition:"${position}",pageCategory:pageCategory},"psp-component":{event:"productSelectPop",clickName:"product select_click to pop_huawei_${position}",clickType:"action",productMktName:"${name}",productPosition:"${position}"},"plp-list":{event:"seriesSectionPop",clickName:"click to pop_huawei_${position}_series_section",clickType:"action",productMktName:"${name}",productPosition:"${position}",pageCategory:pageCategory},"plp-model":{event:"recommendationSectionPop",clickName:"click to pop_huawei_${position}__recommendation_section",clickType:"action",productMktName:"${name}",productPosition:"${position}",pageCategory:pageCategory},"product-list":{event:"listPop",clickName:"product list_click to pop_huawei_${position}",clickType:"action",productMktName:"${name}",productPosition:"${position}"},"product-detail":{event:"productPop",clickName:"product details_click to pop_huawei",clickType:"action",productMktName:"${name}"},"product-detail-footer":{event:"productFooter",clickName:"product details_click to pop_footer",clickType:"action",productMktName:"${name}"},"search-product-detail-footer":{event:"searchBuyToPopFooter",clickName:"site search click to pop footer",clickType:"action",productMktName:"${name}",productPosition:"${position}"},"series-point":{event:"relationSectionPop",clickName:"click to pop_huawei_${position}",clickType:"action",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}"},"series-recommend":{event:"relateProductsPop",clickName:"product list_click to pop_huawei_${position}",clickType:"action",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}"},"site-search":{event:"searchBuyToPopHuawei",clickName:"site search click to pop_huawei",clickType:"action",productMktName:"${name}",productPosition:"${position}"}};
const GA_PSP={navi:{event:"productNavigationPspPosition",clickName:"navigation click to psp_${position}",clickType:"action",productMktName:"${name}",productPosition:"${position}"},banner:{event:"bannerToPsp",clickName:"banner click to psp_${position}",clickType:"action",bannerName:"${name}",bannerPosition:"${position}"},"product-detail":{event:"productChooseToPsp",clickName:"product details click to psp_${name}",clickType:"action",productMktName:"${name}"},"site-search":{event:"searchBuyToPsp",clickName:"site search click to psp",clickType:"action",productMktName:"${name}",productPosition:"${position}"}};
const GA_OPEN_POPUP={navi:{event:"naviIntent",clickName:"header navi_click to pop_intention",clickType:"action",productMktName:"${name}",productPosition:"${position}"},banner:{event:"bannerIntent",clickName:"action",clickType:"banner click to pop_intention_${name}",bannerName:"${name}",bannerPosition:"${position}"},series:{event:"seriesIntent",clickName:"series_click to pop_intention_${position}",clickType:"navigation",productMktName:"${name}",productPosition:"${position}"},relate:{event:"relateProductsIntent",clickName:"product list_click to pop_intention_${position}",clickType:"action",productMktName:"${name}",productPosition:"${position}",pageCategory:pageCategory},"psp-component":{event:"productSelectIntent",clickName:"product select_click to pop_intention_${position}",clickType:"action",productMktName:"${name}",productPosition:"${position}"},"plp-list":{event:"seriesSectionIntent",clickName:"click to pop_intention_${position}_series_section",clickType:"action",productMktName:"${name}",productPosition:"${position}",pageCategory:pageCategory},"plp-model":{event:"recommendationSectionIntent",clickName:"click to pop_intention_${position}__recommendation_section",clickType:"action",productMktName:"${name}",productPosition:"${position}",pageCategory:pageCategory},"product-list":{event:"listIntent",clickName:"product list_click to pop_intention_${position}",clickType:"action",productMktName:"${name}",productPosition:"${position}"},"product-detail":{event:"productIntent",productMktName:"${name}",clickName:"product details_click to pop_intention",clickType:"action"},"series-point":{event:"relationSectionIntent",clickName:"click to pop_intention_${position}",clickType:"action",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}"},"series-recommend":{event:"relateProductsIntent",clickName:"product list_click to pop_intention_${position}",clickType:"action",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}"},"site-search":{event:"searchBuyToPopIntention",clickName:"site search click to pop_intention",clickType:"action",productMktName:"${name}",productPosition:"${position}"}};
const GA_PDP={navi:{event:"naviPdp",productMktName:"${name}",productPosition:"${position}",clickName:"header navi_click to pdp",clickType:"navigation"},banner:{event:"bannerPdp",bannerName:"${name}",bannerPosition:"${position}",clickName:"banner_click to pdp_${name}",clickType:"navigation"},series:{event:"seriesPdp",productMktName:"${name}",productPosition:"${position}",clickName:"series_click to pdp_${position}",clickType:"navigation"},"psp-component":{event:"productSelectClick",productMktName:"${name}",productPosition:"${position}",clickName:"product select_click to pdp_${position}",clickType:"action",pageCategory:pageCategory},"plp-list":{event:"seriesSectionClick",productMktName:"${name}",productPosition:"${position}",clickName:"click to pdp_${position}_series_section",clickType:"action",pageCategory:pageCategory},"plp-model":{event:"recommendationSectionLink",productMktName:"${name}",productPosition:"${position}",clickName:"click to pdp_${position}__recommendation_section",clickType:"action",pageCategory:pageCategory},"product-list":{event:"listPdp",productMktName:"${name}",productPosition:"${position}",clickName:"product list_click to pdp_${position}",clickType:"action"},"series-point":{event:"relationSectionClick",clickName:pageCategory+"_click to series_related_points_${name}_${position}",clickType:"action",pageCategory:pageCategory,bannerName:"series_related_points_${name}",productMktName:"${name}",productPosition:"${position}"},"series-recommend":{event:"relationSectionClick",clickName:pageCategory+"_click to ${name}_${position}",clickType:"action",pageCategory:pageCategory,bannerName:"series_recommend_banner_${name}",productMktName:"${name}",productPosition:"${position}"},"site-search":{event:"relationSectionClick",clickName:pageCategory+"_click to ${name}_${position}",clickType:"action",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}"}};
const GA_PARTNER={navi:{event:"naviPlatform",productMktName:"${name}",productPosition:"top",ecPlatform:"${ecPlatform}",clickName:"header navi_click to pop_${ecPlatform}",clickType:"exit"},banner:{event:"bannerPlatform",bannerName:"${name}",bannerPosition:"${position}",ecPlatform:"${ecPlatform}",clickName:"banner click to pop_${ecPlatform}_${name}",clickType:"action"},series:{event:"SeriesProductPlatform",productMktName:"${name}",ecPlatform:"${ecPlatform}",clickName:"series_click to pop_${ecPlatform}_${position}",clickType:"exit"},relate:{event:"relateProductsPlatform",productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}",clickName:"product list_click to pop_${ecPlatform}_${position}",clickType:"exit",pageCategory:pageCategory},"psp-component":{event:"productSelectPlatform",productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}",clickName:"product select_click to pop_${ecPlatform}_${position}",clickType:"exit"},"plp-list":{event:"seriesSectionPlatform",productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}",clickName:"click to pop_${ecPlatform}_${position}_series_section",clickType:"exit",pageCategory:pageCategory},"plp-model":{event:"recommendationSectionPlatform",productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}",clickName:"click to pop_${ecPlatform}_${position}__recommendation_section",clickType:"exit",pageCategory:pageCategory},"product-list":{event:"listPlatform",productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}",clickName:"product list_click to pop_${ecPlatform}_${position}",clickType:"exit"},"product-detail":{event:"productPlatform",productMktName:"${name}",ecPlatform:"${ecPlatform}",clickName:"product list_click to pop_${ecPlatform}",clickType:"exit"},"series-point":{event:"relationSectionPlatform",clickName:"click to pop_${ecPlatform}_${position}",clickType:"exit",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}"},"series-recommend":{event:"relateProductsPlatform",clickName:"product list_click to pop_${ecPlatform}_${position}",clickType:"exit",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}"},"site-search":{event:"searchBuyToPopEcPlatform",clickName:"site search click to pop_${ecPlatform}",clickType:"exit",productMktName:"${name}",productPosition:"${position}",ecPlatform:"${ecPlatform}"}};
const GA_GLOBAL={navi:{event:"naviEN",productMktName:"${name}",productPosition:"top",countryCode:"${countryCode}",clickName:"header navi_click to pop_${countryCode}",clickType:"action"},banner:{event:"bannerEN",bannerName:"${name}",bannerPosition:"${position}",countryCode:"${countryCode}",clickName:"banner click to pop_${countryCode}_${name}",clickType:"action"},series:{event:"seriesEN",productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}",clickName:"series_click to pop_${countryCode}_${position}",clickType:"navigation"},relate:{event:"relateProductsEN",productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}",clickName:"product list_click to pop_${countryCode}_${position}",clickType:"action",pageCategory:pageCategory},"psp-component":{event:"productSelectEN",productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}",clickName:"product select_click to pop_${countryCode}_${position}",clickType:"action"},"plp-list":{event:"seriesSectionEN",productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}",clickName:"click to pop_${countryCode}_${position}_series_section",clickType:"action",pageCategory:pageCategory},"plp-model":{event:"recommendationSectionEN",productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}",clickName:"click to pop_${countryCode}_${position}__recommendation_section",clickType:"action",pageCategory:pageCategory},"product-list":{event:"listEn",productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}",clickName:"product list_click to pop_${countryCode}_${position}",clickType:"action"},"product-detail":{event:"productEN",productMktName:"${name}",countryCode:"${countryCode}",clickName:"product details_click to pop_${countryCode}",clickType:"action"},"series-point":{event:"relationSectionEN",clickName:"click to pop_${countryCode}_${position}",clickType:"action",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}"},"series-recommend":{event:"relateProductsEN",clickName:"product list_click to pop_${countryCode}_${position}",clickType:"action",pageCategory:pageCategory,productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}"},"site-search":{event:"searchBuyToCountryCode",clickName:"site search click to pop_${countryCode}",clickType:"action",productMktName:"${name}",productPosition:"${position}",countryCode:"${countryCode}"}};
function fillGAData(obj,name,position,ecPlatform,countryCode){var matchs=arguments.callee.toString().match(/\s*function[\w\s]*\(([\w\s,]*)\)/);
var argArray=matchs[1].split(",");
var objStr=JSON.stringify(obj);
for(var i=1;
i<argArray.length;
i++){var arg=argArray[i].trim();
if(eval(arg)){objStr=objStr.replace(new RegExp("\\${"+arg+"}","gm"),eval(arg).replace(new RegExp('"',"gm"),'\\"'))
}}return JSON.parse(objStr)
}var buyToThirdParty_gtm=function(d,b,e,a,f){f=f||false;
var c=f?GA_PSP[e]:GA_THIRD_PARTY[e];
if(c!=null){c=fillGAData(c,d,b);
window.dataLayer.push(addATCommonFields(c))
}if(e.indexOf(DEFAULT_NAVI)!=-1){dmpaCommon("trackEvent","click","navigation interaction",d,a.attr("data-btnlinkinfo"))
}else{if(e.indexOf(DEFAULT_BANNER)!=-1){dmpaCommon("trackEvent","click","banner interaction",d,a.attr("data-btnlinkinfo"))
}}};
var buyOpenPopup_gtm=function(b,a,d){var c=GA_OPEN_POPUP[d];
if(c!=null){c=fillGAData(c,b,a);
window.dataLayer.push(addATCommonFields(c))
}if(d.indexOf(DEFAULT_NAVI)!=-1){dmpaCommon("trackEvent","click","navigation interaction",b,"")
}else{if(d.indexOf(DEFAULT_BANNER)!=-1){dmpaCommon("trackEvent","click","banner interaction",b,"")
}}};
var buyToPdp_gtm=function(b,a,d){var c=GA_PDP[d];
if(c!=null){c=fillGAData(c,b,a);
window.dataLayer.push(addATCommonFields(c))
}};
var buyPartner_gtm=function(b,a,c,e){var d=GA_PARTNER[e];
if(d!=null){d=fillGAData(d,b,a,c);
window.dataLayer.push(addATCommonFields(d))
}};
var buyGlobal_gtm=function(c,a,b,e){var d=GA_GLOBAL[e];
if(d!=null){d=fillGAData(d,c,a,null,b);
window.dataLayer.push(addATCommonFields(d))
}};
function GATool(){$("[data-navicon]").on("click",function(){try{if($(this).parent()&&!$(this).parent().hasClass("third-party-jump")&&$(this).data("navicon")=="to Vmall"){window.dataLayer.push(addATCommonFields({clickName:"account_click cart",clickType:"action",event:"accountInteraction",accountInteraction:"cart",accountType:""}))
}else{var b={event:"firstNavi",iconName:$(this).attr("data-navicon"),clickName:"first navi_click "+$(this).attr("data-navicon"),clickType:"navigation"};
window.dataLayer.push(addATCommonFields(b));
dmpaCommon("trackEvent","click","navigation interaction","firstNavigation",$(this).attr("data-navicon"))
}}catch(a){}});
$("[data-navsecondlink]").on("click",function(){var a={event:"secondNavi",productMktName:$(this).attr("data-navsecondlink"),productPosition:$(this).attr("data-position"),iconName:$(this).attr("data-navsecondlink"),clickName:"second navi_click "+$(this).attr("data-navsecondlink"),clickType:"navigation"};
window.dataLayer.push(addATCommonFields(a));
dmpaCommon("trackEvent","click","navigation interaction",$(this).attr("data-navsecondlink"),$(this).attr("href"))
});
$("[data-mobileservice]").on("click",function(){var a={event:"naviService",serviceMktName:$(this).attr("data-mobileservice"),servicePosition:$(this).attr("data-position"),clickName:"header navi_click to mobileservices",clickType:"navigation"};
window.dataLayer.push(addATCommonFields(a));
dmpaCommon("trackEvent","click","navigation interaction",$(this).attr("data-mobileservice"),$(this).attr("href"))
});
$("[data-navcardlink]").on("click",function(){window.dataLayer.push(addATCommonFields({event:"naviPdp",productMktName:$(this).attr("data-navcardlink"),productPosition:$(this).attr("data-position"),clickName:"header navi_click to pdp",clickType:"navigation"}));
dmpaCommon("trackEvent","click","navigation interaction",$(this).attr("data-navcardlink"),$(this).attr("href"))
});
$("[data-navsupportcard]").on("click",function(){window.dataLayer.push(addATCommonFields({clickName:"header navi_click to product support",clickType:"navigation",event:"naviSupport",productMktName:$(this).attr("data-navsupportcard"),productPosition:$(this).attr("data-position")}));
dmpaCommon("trackEvent","click","navigation interaction",$(this).attr("data-navsupportcard"),$(this).attr("href"))
});
$("[data-social]").on("click",function(){window.dataLayer.push(addATCommonFields({clickName:"social_click "+$(this).attr("data-social"),clickType:"action",event:"social",socialMedia:$(this).attr("data-social")}))
});
$(document).on("click","[data-clicktocall]",function(){window.dataLayer.push({event:"clickToCall",buttonPosition:$(this).attr("data-clicktocall")})
});
$("[data-bannerevent]").on("click",function(a){var g=$(this).attr("data-btntype");
var b=$(this).attr("data-bannerevent");
var c=$(this).attr("href")||"";
var h=c.split("/");
var f="";
var i=b+"_"+$(this).attr("title");
if(b=="hero_carousel"){f=b+"_"+$(".hero-carousel__slider").find(".swiper-slide-active").attr("data-slidename")
}else{var j=c.endsWith("/")&&h.length>2?h[h.length-2]:h[h.length-1];
f=b+"_"+j
}var d={};
if(b=="sub_banner"){if(c.indexOf("?toCampaign")!=-1){d={event:"bannerCampaign",bannerName:"sub_banner_"+$(this).parent().siblings(".sub-banner__title").find("a").attr("title"),bannerPosition:$(this).attr("data-position")};
window.dataLayer.push(addATCommonFields(d))
}else{d={event:"bannerPdp",bannerName:"sub_banner_"+$(this).parent().siblings(".sub-banner__title").find("a").attr("title"),bannerPosition:$(this).attr("data-position")};
window.dataLayer.push(addATCommonFields(d))
}var e="h13-sub-banner_"+$(this).parents(".sub-banne").find(".sub-banner__img a").attr("title");
dmpaCommon("trackEvent","click","banner interaction",e,c)
}else{if(!c.endsWith("/")){c=c+"/"
}if(g=="campaignBtn"||c.indexOf("/campaign/")!=-1||c.indexOf("?toCampaign")!=-1){d={event:"bannerCampaign",bannerName:f,bannerPosition:$(this).attr("data-position"),clickName:"banner click to campaign_"+f,clickType:"navigation"}
}else{if(c.indexOf("/offer/")!=-1){d={event:"bannerOffer",bannerName:f,bannerPosition:$(this).attr("data-position"),clickName:"banner click to offer_"+f,clickType:"navigation"}
}else{d={event:"bannerPdp",bannerName:f,bannerPosition:$(this).attr("data-position"),clickName:"banner click to pdp_"+f,clickType:"navigation"}
}}window.dataLayer.push(addATCommonFields(d));
dmpaCommon("trackEvent","click","banner interaction",i,c)
}a.stopPropagation()
});
$(".sub-banner__item-wrap").on("click",function(c){var b=$(this).find("[data-bannerevent]").attr("href");
var a=$(this).find("[data-bannerevent]").attr("data-position");
if(b!=null&&b.indexOf("?toCampaign")>-1){var d={event:"bannerCampaign",bannerName:"sub_banner_"+$(this).find(".sub-banner__title a").attr("title"),bannerPosition:a};
window.dataLayer.push(addATCommonFields(d))
}else{var d={event:"bannerPdp",bannerName:"sub_banner_"+$(this).find(".sub-banner__title a").attr("title"),bannerPosition:a};
window.dataLayer.push(addATCommonFields(d))
}c.stopPropagation()
});
$("[data-bannerbackimgevent]").on("click",function(d){if(d.target.className.indexOf("global-buy-button")!=-1){d.preventDefault()
}else{var c=$(this).attr("data-btntype");
var b=$(this).attr("data-bannerbackimgevent");
var a=$(this).attr("href");
var g="";
if(a){var f=a.split("/");
if(b=="hero_carousel"){g=b+"_"+$(".hero-carousel__slider").find(".swiper-slide-active").attr("data-slidename")
}else{g=b+"_"+f[f.length-1]
}if(c=="campaignBtn"||(a!=null&&a.indexOf("/campaign/")!=-1)||(a!=null&&a.indexOf("?toCampaign")!=-1)){var e={event:"bannerCampaign",bannerName:g,bannerPosition:$(this).attr("data-position"),clickName:"banner click to campaign_"+g,clickType:"navigation"};
window.dataLayer.push(addATCommonFields(e))
}else{window.dataLayer.push(addATCommonFields({event:"bannerPdp",bannerName:g,bannerPosition:$(this).attr("data-position"),clickName:"banner click to pdp_"+g,clickType:"navigation"}))
}}}});
$(".country-selection__country-wrap").on("click",function(){var a=sessionStorage.getItem("origin_site_path")?sessionStorage.getItem("origin_site_path"):"";
var b={event:"csCountry",clickedCountryCode:$(this).attr("data-selectsitecode"),clickName:"country switch_from "+a+" to "+$(this).attr("data-selectsitecode"),clickType:"navigation",originCountryCode:a};
window.dataLayer.push(addATCommonFields(b));
dmpaCommon("trackEvent","click","country selection",$(this).attr("data-selectsitecode"),$(this).attr("href"))
});
$("[data-bgname]").on("click",function(){var a={event:"bgSwitch",bgName:$(this).attr("data-bgname"),clickName:"switch bg to"+$(this).attr("data-bgname"),clickType:"exit"};
window.dataLayer.push(addATCommonFields(a));
dmpaCommon("trackEvent","click","navigation interaction",$(this).attr("data-bgname"),$(this).attr("href"))
});
$(".signInBtn").on("click",function(){window.dataLayer.push(addATCommonFields({event:"accountInteraction",accountInteraction:"log in",accountType:""}));
dmpaCommon("trackEvent","click","accout","log in","")
});
$(".registeredBtn").on("click",function(){window.dataLayer.push(addATCommonFields({event:"accountInteraction",accountInteraction:"creation",accountType:""}));
dmpaCommon("trackEvent","click","accout","creation","")
});
$(".aboutUsNavi").on("click",function(){var a=$(this).attr("href");
if(a.indexOf("news")>-1){a="news"
}else{a="career"
}window.dataLayer.push(addATCommonFields({clickName:"click to "+a,clickType:"navigation",event:"aboutUsNavi",linkName:a}))
});
$(".signin-service").on("click",function(){window.dataLayer.push(addATCommonFields({clickName:"account_click my service",clickType:"action",event:"accountInteraction",accountInteraction:"my service",accountType:""}));
dmpaCommon("trackEvent","click","accout","my service","")
});
$(".signin-information").on("click",function(){window.dataLayer.push(addATCommonFields({clickName:"account_click my info",clickType:"action",event:"accountInteraction",accountInteraction:"my info",accountType:""}));
dmpaCommon("trackEvent","click","accout","my info","")
});
$(".logout-btn").on("click",function(){window.dataLayer.push(addATCommonFields({clickName:"account_click my log out",clickType:"action",event:"accountInteraction",accountInteraction:"log out",accountType:""}));
dmpaCommon("trackEvent","click","accout","log out","")
});
$(".s02-service-banner .service-banner__link").on("click",function(){var a=$(this).siblings(".service-banner__title").attr("data-title");
window.dataLayer.push(addATCommonFields({clickName:"service_click to "+a,clickType:"navigation",event:"serviceClick",serviceLink:a}))
});
$(".product-tabs__link").on("click",function(){if(!(window.location.href.indexOf("/support")>0)){var e=$("#second-navigation-v4 .product-link__active").attr("data-title")||"";
var a=$(this).attr("data-title");
var b;
var c=window.digitalData.page.category;
if(window.location.href.indexOf("/news/")>-1||window.location.href.indexOf("/video/")>-1){b=c.subCategory1+" page"
}else{if(window.location.href.indexOf("/campaign/")>-1){b=c.primaryCategory+" page"
}else{c.pageType=="product-detail"?b="product details page":b=c.pageType+" page"
}}var d={clickName:"sub header_click to "+a,clickType:"navigation",event:"subHeaderNavigationInteraction",subheaderSection:b,productMktName:e,buttonName:a};
window.dataLayer.push(addATCommonFields(d));
dmpaCommon("trackEvent","click","sub header navigation interaction",b,a)
}});
$(document).on("click","[data-selectedglobalbuy]",function(){var e=$(this).attr("data-nameforga");
var b=$(this).attr("data-selectedglobalbuy");
var f=$(this).attr("data-eventtype");
var a=$(this).attr("data-bannerposition");
buyGlobal_gtm(e,a,b,f);
if(f.indexOf(DEFAULT_NAVI)!=-1){dmpaCommon("trackEvent","click","navigation interaction",e,b)
}else{if(f.indexOf(DEFAULT_BANNER)!=-1){dmpaCommon("trackEvent","click","banner interaction",e,b)
}else{var d=window.digitalData?window.digitalData.page.category.pageType:"";
var c=(d=="product-listing")?"product list interaction":"product details interaction";
dmpaCommon("trackEvent","click",c,getATChapter2(),b)
}}});
$(document).on("click","[data-selectedpartnerbuy]",function(){var e=$(this).attr("data-selectedpartnerbuy");
var d=$(this).attr("data-nameforga");
var f=$(this).attr("data-eventtype");
var a=$(this).attr("data-bannerposition");
buyPartner_gtm(d,a,e,f);
if(f.indexOf(DEFAULT_NAVI)!=-1){dmpaCommon("trackEvent","click","navigation interaction",d,e)
}else{if(f.indexOf(DEFAULT_BANNER)!=-1){dmpaCommon("trackEvent","click","banner interaction",d,e)
}else{var c=window.digitalData?window.digitalData.page.category.pageType:"";
var b=(c=="product-listing")?"product list interaction":"product details interaction";
dmpaCommon("trackEvent","click",b,getATChapter2(),e)
}}});
$(".nav-tolink").attr("href",function(){var a=window.digitalData?window.digitalData.page.pageInfo.siteCode2:"";
var c=$(this).attr("href")||"";
var b=c+(c.indexOf("?")==-1?"?":"&")+"fromConsumer="+a+"_"+pageCategory+"_"+$(this).text();
return b
});
$(".product_buy_btn").on("click",function(){dmpaCommon("trackEvent","click","product list interaction",getATPageName(),$(this).attr("data-btnlinkinfo"))
});
$(".nav-tolink").on("click",function(){var a=$(this).attr("title");
dmpaCommon("trackEvent","click","navigation interaction",a,$(this).attr("href"))
});
$("[data-series-pdp]").on("click",function(){window.dataLayer.push(addATCommonFields({event:"seriesPdp",productMktName:$(this).attr("data-nameforga"),productPosition:$(this).attr("data-position"),clickName:"series_click to pdp_"+$(this).attr("data-position"),clickType:"navigation"}))
});
$("[data-relate-pdp]").on("click",function(){window.dataLayer.push(addATCommonFields({event:"relateProductsPdp",productMktName:$(this).attr("data-nameforga"),productPosition:$(this).attr("data-position"),clickName:"product list_click to pdp_"+$(this).attr("data-position"),clickType:"action",pageCategory:pageCategory}))
});
$(".footer-links__list .footer-links__item").on("click",function(){window.dataLayer.push(addATCommonFields({event:"footerNavi",iconName:$(this).find("a").data("title"),clickName:"foot_click "+$(this).find("a").data("title"),clickType:"action"}))
});
$(".btn.erweimaBTN.a-interaction.a-common").on("click",function(){window.dataLayer.push(addATCommonFields({clickName:"appgallery_click download",clickType:"download",event:"download",buttonName:"appgallery apk",pageName:window.digitalData.page.category.pageType,buttonPosition:"top"}))
});
$(".wrap.text-link__wrap .text-link__download").on("click",function(){try{var a=$(this).text().trim();
window.dataLayer.push(addATCommonFields({clickName:a+"_click download",clickType:"download",event:"download",buttonName:a,pageName:window.digitalData.page.category.pageType,buttonPosition:"bottom"}))
}catch(b){}});
$(".sec .download .pdf").on("click",function(){try{window.dataLayer.push(addATCommonFields({clickName:$(this).text().trim()+"_click download",clickType:"download",event:"download",buttonName:$(this).text().trim(),pageName:window.digitalData.page.category.pageType,buttonPosition:"bottom"}))
}catch(a){}});
$(".productconfigurator").on("click",".weu-btn.weu-btn--primary.js-weu-productconfigurator__buy-btn",function(){try{var a=$(this).attr("lab").trim();
var h={clickName:"product details_click to pop_intention",clickType:"action",event:"productIntent",productMktName:a};
window.dataLayer.push(addATCommonFields(h));
var b=getATPageName(),a=$(this).attr("lab").trim(),d=CBG_SITE_ROOT.substring(0,CBG_SITE_ROOT.length-1)+""+window.location.pathname,c=currentPageName.split(":").length==2?"homepage":window.location.pathname.split(siteCode)[1];
var f={category:"product list interaction",label:b,value:a,location:d,uri:c,subModuleName:"Marketing"};
if(typeof dmpa5!=="undefined"){dmpa5("trackEvent","click",f)
}dmpaCommon("trackEvent","click","product list interaction",getATChapter2(),$(this).attr("href"))
}catch(g){}});
$("[act='header_navigation'][lab='track_order']").on("click",function(){try{window.dataLayer.push(addATCommonFields({clickName:"account_click track order",clickType:"action",event:"accountInteraction",accountInteraction:"track order",accountType:""}))
}catch(a){}});
$(".site_choose_mask .mask_content .site_choose_btn").on("click",function(){try{var a=$(this).data("language");
window.dataLayer.push(addATCommonFields({clickName:"language pop up_click "+a,clickType:"action",event:"languageSelection",buttonName:a}))
}catch(b){}});
$(".site_choose_mask .mask_content #close_btn").on("click",function(){try{window.dataLayer.push(addATCommonFields({clickName:"language pop up_click close",clickType:"action",event:"languageSelection",buttonName:"close"}))
}catch(a){}})
}function dmpaCommon(h,b,f,c,g){var a=window.location.href;
var e=window.digitalData.page.category.pageType==="homepage"?"homepage":window.location.pathname.split(siteCode)[1];
var d={category:f,label:c,value:g,location:a,uri:e,subModuleName:"Marketing"};
if(typeof dmpa5!=="undefined"){dmpa5(h,b,d)
}}$(function(){GATool()
});
(function(){var a={init:function(){var b=this;
if(!$("body").hasClass("huawei-v4")){$("body").addClass("huawei-v4")
}if(("ontouchstart" in window||navigator.msMaxTouchPoints>0)&&window.matchMedia("screen and (max-width: 1199px)").matches){$("html").addClass("touch")
}else{$("html").addClass("no-touch")
}this.dropdown();
this.formElements();
this.browserDetector();
this.detectFocusOnKeyPress();
$(window).on("resize",function(){b.initParallax()
})
},browserDetector:function(){var b=window.navigator.appVersion;
if(b.indexOf("Huawei")!==-1||b.indexOf("HUAWEI")!==-1){$("body").addClass("huawei-device")
}},initParallax:function(){if($(".js-parallax-element").length){var b=null;
if($(window).width()>1199){b=skrollr.init({smoothScrollingDuration:400,forceHeight:false});
if($("html").hasClass("no-touch")){$("html,body").css("overflow","auto")
}}else{if($("html").hasClass("skrollr")&&b){b.destroy()
}}}},dropdown:function(){var h=".js-dropdown-group-option";
var g=".js-dropdown-group";
var e=".js-dropdown-group-btn";
var f=".js-dropdown-group-text";
var b=".js-dropdown-group-list";
var d="dropdown-group__btn--open";
var c="dropdown-group__list-button--selected";
if($(g).length){$(e).on("click",function(){var i=$(this);
if(i.hasClass(d)){i.next().stop().slideUp();
i.removeClass(d)
}else{i.next().stop().delay(150).slideDown(200);
i.addClass(d)
}});
$(h).on("click",function(){var j=$(this);
var i=j.closest(g);
var k=j.text();
i.find(f).text(k);
i.find(e).removeClass(d);
i.find(b).stop().slideUp(200);
j.closest(b).find(h).removeClass(c);
j.addClass(c)
})
}},formElements:function(){if($(".form").length){var b="form__group--focused";
var d="form__group--filled";
var f=$(".form__input--text");
var e=$(".form__input--textarea");
var c=$(".form__input--select");
f.on("focus",function(){$(this).parent().addClass(b)
}).on("blur",function(){$(this).parent().removeClass(b);
if($(this).val()!==""){$(this).parent().addClass(d)
}else{$(this).parent().removeClass(d)
}});
if($("select").length){$("select").selectric({arrowButtonMarkup:'<span class="selectric-arrow"></span>',disableOnMobile:false,responsive:true,forceRenderBelow:true,nativeOnMobile:false,onChange:function(g){$(g).closest(".form__group").addClass(d)
}});
$(".selectric-input").wrap('<label class="sr-only" aria-hidden="true"></label>')
}if(e.length){e.each(function(){var h=$(this);
var g=h.data("max-characters");
if(g!=="undefined"){if(!h.siblings(".form__max-characters").length){h.after('<span class="form__max-characters"><span class="current">0</span>/<span class="max">'+g+"</span></span>")
}}h.on("focus",function(){$(this).parent().addClass(b)
}).on("blur",function(){$(this).parent().removeClass(b);
if($(this).val()!==""){$(this).parent().addClass(d)
}else{$(this).parent().removeClass(d)
}}).on("keydown keyup",function(){var i=$(this).val().length;
if(i>g){$(this).val($(this).val().substring(0,g))
}else{$(this).siblings(".form__max-characters").find(".current").text(i)
}})
})
}}},detectFocusOnKeyPress:function(){var b="active-focus";
$(document).on("keydown",function(d){var c=d.keyCode||d.which;
if(c===9){$("body").addClass(b)
}});
$(document).on("click",function(){if($("body").hasClass(b)){$("body").removeClass(b)
}})
}};
$(function(){a.init()
});
$(window).on("load",function(){setTimeout(function(){$("html").addClass("loaded");
a.initParallax()
},10)
})
}());
(function(){var a={$selector:$(".n04-platform-selection"),$platformToggle:$(".platform-selection__toggle"),$plateformClose:$(".n04-platform-selection .icon-close"),$platformContent:$(".platform-selection__content"),platformSelectionOpenedClass:"platform-selection--opened",platformToggleOpenedClass:"platform-selection__toggle--opened",platformToggleDisabledClass:"platform-selection__toggle--disabled",$secondNav:$("#second-navigation-v4"),$newsSecondNav:$("#news-second-navigation-v4"),$headerNav:$(".v4.header"),$headerPl:$(".header-placeholder"),$mainNav:$(".header .n01-main-navigation"),headerNavFlag:true,$ipJump:$(".ip-jump-wrap"),navVersion:$("#header-v4 #mainNav").val()||"nav-v1",uiBoundaryVal:1200,init:function(){this.uiBoundaryVal=this.navVersion=="nav-v1"?1200:1366;
if(this.$selector.length){this.togglePlatform()
}this.handlePlatformContainer();
this.addOutline()
},addOutline:function(){var b=this;
$(".dropdown__card_link_btn").on("focus",function(){$(this).parent().siblings(".btn").addClass("h-active-btn");
$(this).parent().parent().addClass("h-active-btns");
$(this).parent().siblings(".btn").last().on("blur",function(){$(this).parent().children(".btn").removeClass("h-active-btn");
$(this).parent().removeClass("h-active-btns")
})
});
$(".dropdown__card_link_btn").on("focus",function(){$(this).parent().css("border","1px solid #d20a2c")
});
$(".dropdown__card_link_btn").on("blur",function(){$(this).parent().css("border","none")
});
$(".h-dropdown__card_link").on("focus",function(){$(this).children().css("border","1px solid #d20a2c")
});
$(".h-dropdown__card_link").on("blur",function(){$(this).children().css("border","none")
});
$(window).on("load resize",function(){if(window.innerWidth<b.uiBoundaryVal||b.$headerNav.hasClass("mb-ui")){$(".dropdown__order").each(function(){$(this).insertBefore($(this).siblings())
})
}else{$(".dropdown__order").each(function(){$(this).insertAfter($(this).siblings())
})
}})
},handlePlatformContainer:function(){var b=this;
if(window.pageCategory=="homepage"&&window.innerWidth>=b.uiBoundaryVal&&!b.$headerNav.hasClass("mb-ui")){b.handleInitTop(b);
window.addEventListener("scroll",function(){b.handleInitTop(b)
})
}window.addEventListener("scroll",function(){var c=document.documentElement.scrollTop||document.body.scrollTop;
if(c>1){if(b.$headerNav.hasClass("header-scroll")){return
}b.$headerNav.addClass("header-scroll")
}else{if(c<1){b.$headerNav.removeClass("header-scroll")
}}})
},handleInitTop:function(f){var b=navigator.userAgent.toLowerCase();
var e=!!window.ActiveXObject?!!window.ActiveXObject:"ActiveXObject" in window,c=b.toUpperCase().indexOf("MSIE")>-1;
var d=document.documentElement.scrollTop||document.body.scrollTop;
if(f.$selector.length){if(d>1&&f.headerNavFlag){f.headerNavFlag=false;
f.$headerNav.addClass("header-move");
f.$headerPl.addClass("header-placeholder-pl");
if(!f.$platformToggle.hasClass(f.platformToggleDisabledClass)){if(f.$platformToggle.hasClass(f.platformToggleOpenedClass)){f.$platformToggle.removeClass(f.platformToggleOpenedClass);
$(this).attr("aria-expanded",false);
f.$platformContent.stop().slideUp(400,function(){f.$selector.removeClass(f.platformSelectionOpenedClass)
})
}}if(e||c){$(".n12-search").addClass("header-move")
}}else{if(d<1&&!f.headerNavFlag){f.headerNavFlag=true;
f.$headerNav.removeClass("header-move");
f.$headerPl.removeClass("header-placeholder-pl");
if(e||c){$(".n12-search").removeClass("header-move")
}}}}else{if(d>1&&f.headerNavFlag){f.headerNavFlag=false;
$(".v4.n01-main-navigation").addClass("main-navigation_white")
}else{if(d<1&&!f.headerNavFlag){f.headerNavFlag=true;
$(".v4.n01-main-navigation").removeClass("main-navigation_white")
}}}},togglePlatform:function(){var b=this;
b.$platformToggle.on("click",function(){if(!$(this).hasClass(b.platformToggleDisabledClass)){if(!$(this).hasClass(b.platformToggleOpenedClass)){$(this).addClass(b.platformToggleOpenedClass);
$(this).attr("aria-expanded",true);
$(this).siblings().find("a[href]").last().on("blur",function(){$(this).parents(".platform-selection__content").siblings().focus()
});
b.showPlatformSelection()
}else{$(this).removeClass(b.platformToggleOpenedClass);
$(this).attr("aria-expanded",false);
b.closePlatformSelection()
}}});
b.$plateformClose.on("click",function(){b.$platformToggle.removeClass(b.platformToggleOpenedClass);
b.closePlatformSelection()
})
},showPlatformSelection:function(){var e=this;
var b=$(".main-nav").find(".popup");
var c=$("#header-v4").height();
var d=0;
if($(".platform-selection__content").length){d=$(".platform-selection__content").height()
}e.$selector.addClass(e.platformSelectionOpenedClass);
e.adaptPageUI();
e.closeFilter();
if($(".plp-series-list.js-nav-fixed").length){$(".productnav").addClass("js-select-opened");
$(".productnav").animate({top:c+d},150);
if($(".js-fixed-position").length){$(".js-fixed-position").animate({top:c+d},600)
}}setTimeout(function(){e.$platformContent.stop().slideDown(500);
if(window.innerWidth<e.uiBoundaryVal||e.$headerNav.hasClass("mb-ui")){if(b.is(":visible")){b.slideUp(400)
}$(".main-nav__link--opened").attr("aria-expanded",false);
$(".main-nav__link--opened").removeClass("main-nav__link--opened")
}},20)
},adaptPageUI:function(){var e=this;
if(Mkt.Util.windowWidth()<e.uiBoundaryVal||e.$headerNav.hasClass("mb-ui")){var c=e.$headerNav.innerHeight();
if($("#locationSecret").is(":visible")){var d=$("#locationSecret").height();
c+=d
}var b=e.$mainNav.height();
e.$selector.css("height","calc(100% - "+(c-b)+"px")
}},closePlatformSelection:function(){var c=this;
var b=$("#header-v4").height();
if($(".plp-series-list.js-nav-fixed").length){$(".productnav").removeClass("js-select-opened");
$(".productnav").animate({top:b},50);
if($(".js-fixed-position").length){$(".js-fixed-position").animate({top:b},400)
}}c.$platformContent.stop().slideUp(400,function(){c.$selector.removeClass(c.platformSelectionOpenedClass)
});
if(window.innerWidth<c.uiBoundaryVal||c.$headerNav.hasClass("mb-ui")){c.$selector.removeAttr("style")
}},closeFilter:function(){$(".js-pf-content").removeClass("product-filter__container--visible");
$(".js-pf-button").removeClass("product-filter__button--expanded");
$(".js-pf-items").stop().slideUp()
}};
$(function(){a.init()
})
}());
(function(){var b={$headerNav:$(".v4.header"),$selector:$(".n01-main-navigation"),$mainNav:$(".main-nav"),mainNavOpenedClass:"main-nav--opened",mainNavItem:".main-nav__item",mainNavItemVisibleClass:"main-nav__item--visible",navLink:".main-nav__link",navLinkOpenedClass:"main-nav__link--opened",navLinkTransparentClass:"main-nav__link--transparent",searchOpenBtn:".js-open-search",searchPopup:".n12-search",openedSearch:false,$loginV4:$(".login-v4-wrap"),$loginV4OpenedClass:"active",$ipJump:$(".ip-jump-wrap"),popup:".popup",popupCloseBtn:".js-close-popup",popupVisibleClass:"popup--visible",header:".header",popupOpenedClass:"header--popup-opened",popupOpenedTimer:null,isPopupOpened:false,$navToggle:$(".js-nav-toggle"),navToggleActiveClass:"nav-toggle--active",$platformToggle:$(".js-platform-toggle"),$platformModule:$(".platform-selection"),$platformContent:$(".platform-selection__content"),platformToggleVisibleClass:"platform-selection__toggle--visible",platformToggleOpenedClass:"platform-selection__toggle--opened",platformToggleDisabledClass:"platform-selection__toggle--disabled",navVersion:$("#header-v4 #mainNav").val()||"nav-v1",uiBoundaryVal:1200,pcLfNavW:0,pcRgNavW:0,pcAddonsW:0,otherAreaW:0,topScroll:0,isScrollDisabled:false,scrollTimer:null,pageTypeNavFlag:false,init:function(){var d=this;
d.uiBoundaryVal=d.navVersion=="nav-v1"?1200:1366;
if(this.$selector.length){this.calcNewUIBoundaryVal();
this.calcMainNavWidth();
this.navLinksHover();
this.bindNavLinkClick();
this.bindSearchClick();
this.bindClosePopupClick();
this.bindNavToggleClick();
this.bindLoginToggleClick();
this.bindIpJump()
}},calcNewUIBoundaryVal:function(){var i=Mkt.Util.windowWidth();
if(this.navVersion=="nav-v2"&&i>1365){var f=$(".v4.n01-main-navigation.nav-v2 .main-nav .lf-nav");
var e=$(".v4.n01-main-navigation.nav-v2 .main-nav .rg-nav");
this.pcLfNavW=Math.round(f.width());
this.pcRgNavW=Math.round(e.width());
var g=$(".v4.n01-main-navigation.nav-v2 .nav-addons");
this.pcAddonsW=Math.round(g.width());
var h=80;
if(i<1600&&i>=768){h=40
}var d=110+64+40;
this.uiBoundaryVal=this.pcLfNavW+this.pcRgNavW+this.pcAddonsW+d+h*2;
this.otherAreaW=this.pcAddonsW+d+h*2
}},calcMainNavWidth:function(){var f=this;
if(f.navVersion=="nav-v2"){var e=Mkt.Util.windowWidth();
if(e>1365){if(e<f.uiBoundaryVal){$("#header-v4,#header-placeholder").addClass("mb-ui");
$(".v4.n01-main-navigation.nav-v2 .main-nav").width("100%");
var d=$("#header-v4").innerHeight();
$("#header-placeholder").css({height:d});
$(".v4.n01-main-navigation.nav-v2 .main-nav,.huawei-v4 .login-v4-wrap .login-v4,.v4.n12-search").css("top",d);
f.pcHorizontalDrag()
}else{$(".v4.n01-main-navigation.nav-v2 .main-nav").width("100%");
$("#header-v4,#header-placeholder").removeClass("mb-ui")
}}else{$("#header-v4,#header-placeholder").removeClass("mb-ui")
}if(e>=1200&&e<1366){f.pcHorizontalDrag()
}}},navLinksHover:function(){var d=this;
this.$mainNav.find(d.popup).each(function(){$(this).parent().addClass("main-nav__item--has-children");
$(this).siblings("a").attr("role","menuitem");
$(this).siblings("a").attr("aria-expanded",false);
$(this).siblings("a").attr("aria-haspopup",true)
});
$(this.navLink).hover(function(){if(!d.isPopupOpened&&window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){if(d.navVersion=="nav-v1"){$(this).parent().siblings().find(d.navLink).addClass(d.navLinkTransparentClass)
}}},function(){if(!d.isPopupOpened&&window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){$(this).addClass("unhover");
d.$mainNav.find("."+d.navLinkTransparentClass).removeClass(d.navLinkTransparentClass)
}})
},bindNavLinkClick:function(){var d=this;
$(document).on("click",d.navLink,function(h){var f=$(this);
var g=f.siblings(d.popup);
clearTimeout(d.popupOpenedTimer);
d.openedSearch=false;
g.find("img.lazyload-img").each(function(){$(this).attr("src",$(this).attr("data-src")).removeClass("lazyload-img")
});
if(window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){if(d.pageTypeNavFlag){if($("#header-v4").hasClass("minisite-nav")){$("#header-v4").toggleClass("minisite-nav")
}else{$("#header-v4").toggleClass("minisite-nav")
}}if(!f.hasClass(d.navLinkOpenedClass)){d.closeAllPopups(false)
}else{d.closeAllPopups(true)
}}if(g.length){if(window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){if(f.hasClass(d.navLinkOpenedClass)){f.removeClass(d.navLinkOpenedClass);
f.attr("aria-expanded",false);
g.removeClass(d.popupVisibleClass);
$(".js-open-search").attr("aria-expanded",false);
$(d.header).removeClass(d.popupOpenedClass);
d.isPopupOpened=false;
d.removeUnScroll();
d.enableScroll()
}else{d.isPopupOpened=true;
d.unScroll();
d.disableScroll();
f.addClass(d.navLinkOpenedClass);
f.attr("aria-expanded",true);
g.addClass(d.popupVisibleClass);
$(".n02-expanded-products.popup--visible,.n03-expanded-support.popup--visible").find("a[href]").last().on("blur",function(){$(this).parents(".dropdown").siblings(".popup__close-btn").focus()
});
if(d.navVersion=="nav-v1"){f.parent().siblings().find(d.navLink).addClass(d.navLinkTransparentClass)
}d.$platformToggle.removeClass(d.platformToggleOpenedClass).addClass(d.platformToggleDisabledClass);
d.$platformContent.stop().slideUp(200);
if(!$(d.header).hasClass(d.popupOpenedClass)){d.popupOpenedTimer=setTimeout(function(){$(d.header).addClass(d.popupOpenedClass)
},600)
}$(".dropdown__btns").siblings(".dropdown__card_link_btn").attr("tabindex",-1);
$(".dropdown__left").find(".dropdown__big-link").first().on("blur",function(){$(".mCSB_outside").length>0&&$(".mCSB_outside").attr("tabindex",-1)
})
}setTimeout(function(){d.customScrollBarProducts()
},500)
}else{if(f.hasClass(d.navLinkOpenedClass)){f.removeClass(d.navLinkOpenedClass);
f.attr("aria-expanded",false);
g.stop().slideUp(400)
}else{$("."+d.navLinkOpenedClass).siblings(d.popup).stop().slideUp(400);
$("."+d.navLinkOpenedClass).attr("aria-expanded",false);
$("."+d.navLinkOpenedClass).removeClass(d.navLinkOpenedClass);
f.addClass(d.navLinkOpenedClass);
f.attr("aria-expanded",true);
$(".dropdown__btns").siblings(".dropdown__card_link_btn").attr("tabindex",0);
g.stop().slideDown(500)
}}}else{if($(d.header).hasClass(d.popupOpenedClass)){$(d.header).removeClass(d.popupOpenedClass);
d.removeUnScroll();
d.enableScroll()
}}})
},bindSearchClick:function(){var d=this;
$(document).on("click",d.searchOpenBtn,function(){if($(d.searchPopup).length){if(!d.openedSearch){var e=$("#header-v4").innerHeight();
d.openedSearch=false;
d.closeAllPopups(false);
setTimeout(function(){$(d.searchPopup).addClass(d.popupVisibleClass);
$(".js-open-search").attr("aria-expanded",true);
$(".n12-search.popup").find("a:visible[href]").last().on("blur",function(){if(window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){$(".js-close-popup").focus()
}else{$(".js-open-search").focus()
}});
$(".login-v4-wrap,.js-nav-toggle,.shop-bag-bnt,.logo").attr("tabindex",-1);
d.openedSearch=true;
if(window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){d.unScroll()
}d.disableScroll();
setTimeout(function(){if(d.openedSearch){$(d.header).addClass(d.popupOpenedClass)
}},550)
},50);
if(window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){d.$platformToggle.removeClass(d.platformToggleOpenedClass).addClass(d.platformToggleDisabledClass);
d.$platformContent.stop().slideUp(200)
}}else{$(d.searchPopup).removeClass(d.popupVisibleClass);
$(".js-open-search").attr("aria-expanded",false);
$(".login-v4-wrap,.js-nav-toggle,.shop-bag-bnt,.logo").attr("tabindex",0);
$(d.header).removeClass(d.popupOpenedClass);
d.openedSearch=false;
d.removeUnScroll();
d.enableScroll();
d.closeAllPopups()
}if(d.$mainNav.hasClass(d.mainNavOpenedClass)){d.$mainNav.removeClass(d.mainNavOpenedClass);
d.$mainNav.find(d.mainNavItem).removeClass(d.mainNavItemVisibleClass);
d.$navToggle.removeClass(d.navToggleActiveClass);
d.$navToggle.attr("aria-expanded",false)
}if(window.innerWidth<d.uiBoundaryVal||d.$headerNav.hasClass("mb-ui")){if(d.$loginV4.hasClass(d.$loginV4OpenedClass)){$(d.$loginV4).removeClass(d.$loginV4OpenedClass);
$(d.$loginV4).attr("aria-expanded",false)
}}}})
},bindClosePopupClick:function(){var d=this;
$(".main-nav__item").on("blur",function(){$(this).removeAttr("tabindex")
});
$(document).on("click",d.popupCloseBtn,function(){$(this).parents(".main-nav__item").attr("tabindex",-1);
$(this).parents(".main-nav__item").focus();
$(this).parents(".main-nav__item").find(".main-nav__link").on("blur",function(){if($(this).attr("aria-expanded")=="false"){$(this).parents(".main-nav__item").next().find(".main-nav__link").focus()
}});
$(d.header).removeClass(d.popupOpenedClass);
d.closeAllPopups(false);
d.openedSearch=false;
d.removeUnScroll();
d.enableScroll()
});
$(".n12-search .js-close-popup").on("click",function(){$(".nav-addons").attr("tabindex",-1);
$(".nav-addons").focus();
$(".login-v4-wrap,.js-nav-toggle,.shop-bag-bnt,.logo").attr("tabindex",0)
})
},closeAllPopups:function(d){$(this.popup).removeClass(this.popupVisibleClass);
$(".js-open-search").attr("aria-expanded",false);
if(this.$platformToggle.hasClass(this.platformToggleDisabledClass)){this.$platformToggle.removeClass(this.platformToggleDisabledClass)
}if(!d){this.isPopupOpened=false;
var f=$("."+this.navLinkTransparentClass);
if(f.length){f.removeClass(this.navLinkTransparentClass)
}var e=$("."+this.navLinkOpenedClass);
if(e.length){e.removeClass(this.navLinkOpenedClass);
e.attr("aria-expanded",false)
}}setTimeout(function(){this.openedSearch=false
},25)
},bindNavToggleClick:function(){var d=this;
d.$navToggle.on("click",function(){d.closeAllPopups(true);
$(this).toggleClass(d.navToggleActiveClass);
d.$mainNav.toggleClass(d.mainNavOpenedClass);
$(d.header).removeClass(d.popupOpenedClass);
if($(this).hasClass(d.navToggleActiveClass)){$(".login-v4-wrap,.nav-addons__search,.shop-bag-bnt,.logo").attr("tabindex",-1);
$(this).on("blur",function(){if(window.innerWidth>d.uiBoundaryVal){$(".main-nav").find("a:visible[href]").first().trigger("focus")
}else{$(".main-nav.main-nav--opened").attr("tabindex",-1).css("outline","0px");
$(".main-nav.main-nav--opened").focus()
}});
$(this).attr("aria-expanded","true");
if(window.innerWidth<d.uiBoundaryVal||d.$headerNav.hasClass("mb-ui")){d.$mainNav.find(d.mainNavItem).each(function(f){var e=$(this);
setTimeout(function(){e.addClass(d.mainNavItemVisibleClass)
},f*100+300)
});
d.$platformToggle.addClass(d.platformToggleVisibleClass)
}d.disableScroll();
d.unScroll();
d.$loginV4.removeClass(d.$loginV4OpenedClass);
d.$loginV4.attr("aria-expanded",false)
}else{$(".login-v4-wrap,.nav-addons__search,.shop-bag-bnt,.logo").attr("tabindex",0);
$(this).unbind("blur");
$(this).attr("aria-expanded","false");
d.$mainNav.find(d.mainNavItem).removeClass(d.mainNavItemVisibleClass);
d.$platformToggle.removeClass(d.platformToggleVisibleClass);
d.enableScroll();
d.removeUnScroll()
}setTimeout(function(){d.openedSearch=false
},25)
})
},bindLoginToggleClick:function(){var g=this;
var f="";
$(".login-v4-cnt").find("a:visible[href]").last().on("blur",function(){$(".login-v4-wrap").attr("tabindex",0);
$(".login-v4-wrap").focus()
});
if(window.innerWidth>=g.uiBoundaryVal&&!g.$headerNav.hasClass("mb-ui")){var d=function(h){event.stopPropagation();
$(".ec-mc").hasClass("on")?$(".ec-mc").removeClass("on"):"";
if(h.hasClass(g.$loginV4OpenedClass)){h.removeClass(g.$loginV4OpenedClass);
h.attr("aria-expanded",false)
}else{h.addClass(g.$loginV4OpenedClass);
h.attr("aria-expanded",true)
}};
g.$loginV4.bind("keydown",function(h){if(h.keyCode==13){d($(this))
}});
$(".shop-bag").bind("keydown",function(h){if(h.keyCode==13){$(this).click()
}});
if(isECommerceSite=="Fusion-eCommerce"){g.$loginV4.bind("click",function(h){d($(this))
});
$("body").on("click").click(function(h){var i=$(h.target);
if(i.hasClass("font-ico-profile")){return
}else{$(".Fusion-eCommerce").removeClass("active")
}});
$(".login-v4-cnt").on("click",function(h){h=h||window.event;
h.stopPropagation()
})
}else{g.$loginV4.on("mouseenter",function(h){h.stopPropagation();
$(this).addClass(g.$loginV4OpenedClass);
$(this).attr("aria-expanded",true);
clearTimeout(f)
});
g.$loginV4.on("mouseleave",function(h){h.stopPropagation();
var i=$(this);
f=setTimeout(function(){i.removeClass(g.$loginV4OpenedClass);
i.attr("aria-expanded",false)
},300)
})
}}else{var e=function(i){g.closeAllPopups(true);
if(g.$ipJump.is(":visible")){if($("#locationSecret").is(":visible")){var h=$("#header-v4").innerHeight();
$(".login-v4").css("top",h+"px")
}else{var h=$("#header-v4").height();
$(".login-v4").css("top",h+"px")
}}else{if($("#locationSecret").is(":visible")){var h=$("#header-v4").innerHeight();
$(".login-v4").css("top",h+"px")
}}i.toggleClass(g.$loginV4OpenedClass);
if(i.hasClass(g.$loginV4OpenedClass)){g.$mainNav.removeClass(g.mainNavOpenedClass);
g.$navToggle.removeClass(g.navToggleActiveClass);
g.$navToggle.attr("aria-expanded",false);
g.disableScroll();
g.unScroll();
i.attr("aria-expanded",true);
$(".login-v4-wrap").removeAttr("tabindex")
}else{g.enableScroll();
g.removeUnScroll();
i.attr("aria-expanded",false);
$(".login-v4-wrap").attr("tabindex",0)
}setTimeout(function(){g.openedSearch=false
},25)
};
g.$loginV4.on("click",function(){e($(this))
});
g.$loginV4.on("keydown",function(h){if(h.keyCode==13){e($(this))
}})
}},bindIpJump:function(){var f=this;
var d=$(".main-nav").find(".popup");
if(f.$ipJump.is(":visible")){var e=$("#header-v4").height();
$("#header-placeholder").css("height",e+"px");
$("#header-v4").addClass("hasIp");
$(".page-plp").addClass("hasIp");
if(window.innerWidth>=f.uiBoundaryVal&&!f.$headerNav.hasClass("mb-ui")){d.css("top",e+"px")
}if(window.innerWidth<f.uiBoundaryVal||f.$headerNav.hasClass("mb-ui")){if($("#locationSecret").is(":visible")){var e=$("#header-v4").innerHeight();
f.$mainNav.css("top",e+"px")
}else{f.$mainNav.css("top",e+"px")
}}}else{if(window.innerWidth<f.uiBoundaryVal||f.$headerNav.hasClass("mb-ui")){if($("#locationSecret").is(":visible")){var e=$("#header-v4").innerHeight();
f.$mainNav.css("top",e+"px")
}}}},customScrollBarProducts:function(){if(window.innerWidth>=this.uiBoundaryVal){this.$selector.find(".dropdown__right").mCustomScrollbar({axis:"y",scrollbarPosition:"outside"})
}else{this.$selector.find(".dropdown__right").mCustomScrollbar("destroy")
}},disableScroll:function(){if(!this.isScrollDisabled){this.topScroll=$(window).scrollTop();
if(window.innerWidth<this.uiBoundaryVal){$("body").addClass("scroll-disabled").css("top",-this.topScroll+"px");
if($("#second-navigation-v4").length){$("#header-v4").css("position","fixed")
}}if($("#second-navigation-v4").length){$(window).scrollTop(0)
}this.isScrollDisabled=true
}},enableScroll:function(){if(this.isScrollDisabled){if(window.innerWidth<this.uiBoundaryVal){$("body").css("top","0px").removeClass("scroll-disabled");
$(window).scrollTop(this.topScroll);
if($("#second-navigation-v4").length){$("#header-v4").css("position","absolute")
}}else{$(window).scrollTop(this.topScroll)
}this.isScrollDisabled=false
}},unScroll:function(){var d=this;
$(window).on("scroll",d.scrollClosePopups);
if(window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")&&!d.$selector.hasClass("list-navigation")){if(typeof window.onmousewheel=="object"){window.addEventListener("mousewheel",d.stopScroll,{passive:false});
window.addEventListener("mousewheel",d.scrollClosePopups,{passive:false})
}else{window.addEventListener("DOMMouseScroll",d.stopScroll,{passive:false});
window.addEventListener("DOMMouseScroll",d.scrollClosePopups,{passive:false})
}}},removeUnScroll:function(){var d=this;
if(window.innerWidth>=d.uiBoundaryVal&&!d.$headerNav.hasClass("mb-ui")){$(window).off("scroll",d.scrollClosePopups);
if(typeof window.onmousewheel=="object"){window.removeEventListener("mousewheel",this.stopScroll,{passive:false});
window.removeEventListener("mousewheel",this.scrollClosePopups,{passive:false})
}else{window.removeEventListener("DOMMouseScroll",this.stopScroll,{passive:false});
window.removeEventListener("DOMMouseScroll",this.scrollClosePopups,{passive:false})
}}},scrollClosePopups:function(){if($(b.header).hasClass(b.popupOpenedClass)){clearTimeout(b.scrollTimer);
b.scrollTimer=setTimeout(function(){b.handleClosePopup()
},300)
}},handleClosePopup:function(){this.closeAllPopups(false);
if(this.pageTypeNavFlag){if($("#header-v4").hasClass("minisite-nav")){$("#header-v4").toggleClass("minisite-nav")
}else{$("#header-v4").toggleClass("minisite-nav")
}}$(this.header).removeClass(this.popupOpenedClass);
$(this.searchPopup).removeClass(this.popupVisibleClass);
$(".js-open-search").attr("aria-expanded",false);
this.openedSearch=false;
this.isScrollDisabled=false;
this.removeUnScroll()
},stopScroll:function(d){if(d.preventDefault){d.preventDefault()
}else{d.returnValue=false
}},pcHorizontalDrag:function(){var g=$(".main-navigation.nav-v2 .v4.n02-expanded-products .dropdown__wrap .dropdown__right,.main-navigation.nav-v2 .v4.n03-expanded-support .dropdown__right");
g.on("mousedown",h);
var i=0,e=0;
function h(j){if(j.button===0){i=j.clientX;
e=$(this).scrollLeft();
$(document).on("mousemove",d);
$(document).on("mouseup",f)
}return false
}function d(j){var k=j.clientX-i;
g.scrollLeft(e-k);
return false
}function f(){$(document).off("mousemove",d);
$(document).off("mouseup",f)
}}};
var a={$secondEle:$("#second-navigation-v4"),dropDownbtn:"#second-navigation-v4 .drop-down__btn",buyBtn:"#second-nav-buy-button",product:null,secNavItem:null,secNavItemDropDown:null,init:function(){if(window.integrationJsInterface||window.integrationJsInterfaceWebview){if(siteCode==="en"){this.$secondEle.hide();
return
}}var d=this;
if(this.$secondEle.length){this.bindNavToggle();
this.bindDropDownClick();
this.initBuyButton();
this.focusOnActive();
this.bindGAListener();
this.bindNavDropdownToggle();
$(window).resize(function(){d.setDropdownPosition()
})
}},bindGAListener:function(){var d=this;
this.$secondEle.find(".relate-product").on("click",function(f){window.dataLayer.push(addATCommonFields({clickName:"sub header navi_click to "+$(this).attr("title"),clickType:"action",event:"subHeaderNaviClick",pageCategory:window.digitalData.page.category.pageType,productMktName:d.$secondEle.find(".product-link__active").data("title"),buttonName:$(this).attr("title")}))
});
this.$secondEle.find(".dropdown-link").on("click",function(f){window.dataLayer.push(addATCommonFields({clickName:"sub header_click to "+$(this).closest(".sec-nav-item-dropDown").data("parent")+"_"+$(this).attr("title"),clickType:"action",event:"subHeaderNaviSupportChildMenu",subheaderSection:"support page",pageCategory:window.digitalData.page.category.pageType,productMktName:d.$secondEle.find(".product-link__active").data("title"),buttonName:$(this).closest(".sec-nav-item-dropDown").data("parent"),subButtonName:$(this).attr("title")}))
})
},setDropdownPosition:function(){if(!this.secNavItem&&!this.secNavItemDropDown){return
}var d=this.secNavItem.offset();
var e=d.left-(this.secNavItemDropDown.innerWidth()-this.secNavItem.innerWidth())/2;
var f=$("#second-navigation-v4").height();
if($(window).width()>975){this.secNavItemDropDown.offset({left:e})
}else{this.secNavItemDropDown.offset({left:0})
}},bindNavDropdownToggle:function(){var d=this;
$(document).on("click",".product-tabs__links-item.with-drop-down-config",function(){d.secNavItem=$(this);
var e=d.secNavItem.find("a").attr("data-index");
d.secNavItemDropDown=$('[data-relate="'+e+'"]');
d.setDropdownPosition();
if(window.pageType==="support"){(!d.secNavItemDropDown.hasClass("dif-padding"))&&d.secNavItemDropDown.addClass("dif-padding")
}d.secNavItemDropDown.slideToggle(700);
d.secNavItem.toggleClass("unfold-status");
d.secNavItem.children("i").toggleClass("reverse");
var f=$("#second-navigation-v4 .drop-down__btn,#second-navigation-v4 .drop-down__wrap");
if(f.length>0&&f.hasClass("open")){f.removeClass("open");
$("#second-navigation-v4 .drop-down__wrap").slideUp(700)
}});
$(document).on("click",function(g){var f=$(g.target);
if(f.closest(".with-drop-down-config").length==0){$(".sec-nav-item-arrow-icon").removeClass("reverse");
d.secNavItem&&d.secNavItem.removeClass("unfold-status");
d.secNavItemDropDown&&d.secNavItemDropDown.slideUp(700)
}})
},focusOnActive:function(){var d=$("#second-navigation-v4 .product-tabs__link--active");
if(d.length){var g=d.parents().eq(2).width();
var e=d.parent().position().left;
var f=d.parent().width();
if(e<0){d.parents().eq(2).animate({scrollLeft:e},400)
}if(e>=0&&g<e+f){d.parents().eq(2).animate({scrollLeft:e},400)
}}},initBuyButton:function(){var g=$(this.buyBtn);
if(g.length==0){return
}var j=$("#second-navigation-v4").find("#buy-wrap input[name='productJson']").val();
var l=$("#second-navigation-v4").find("#buy-wrap input[name='showStoreFinder']").val()=="true";
var e=$("#second-navigation-v4").find("#buy-wrap input[name='storeFinderLink']").val();
var f=$("#second-navigation-v4").find("#buy-wrap input[name='openStoreFinderInNewPage']").val();
var i=$("#second-navigation-v4").find("#buy-wrap input[name='disclaimer']").val();
var h=$("#second-navigation-v4").find("#buy-wrap input[name='enablePdpFusion']").val()=="true";
this.product=JSON.parse(j);
var k=this.product.ecBuyLink;
buyBtnAttributes(this.product,this.product.marketingName,"second_top","product-detail");
for(var d in this.product.buyButtonAttr){g.attr(d,this.product.buyButtonAttr[d])
}g.on("click",function(){if((window.integrationJsInterface||window.integrationJsInterfaceWebview)&&h){window.open(k,"_self")
}else{var n=$(this).attr("data-pname")||"";
var m={showStoreFinder:l,openStoreFinderInNewPage:f,storeFinderLink:e};
buyFeature($(this),m,i,n);
dmpaCommon("trackEvent","click","product details interaction",getATChapter2(),$(this).attr("data-btnlinkinfo"))
}})
},bindDropDownClick:function(){var d=this;
if($(d.dropDownbtn).length){$(document).on("click",d.dropDownbtn,function(){$("#second-navigation-v4 .drop-down__btn,#second-navigation-v4 .drop-down__wrap").toggleClass("open");
$("#second-navigation-v4 .drop-down__wrap").slideToggle(700);
window.dataLayer.push(addATCommonFields({clickName:"sub header navi_click drop down button",clickType:"action",event:"subHeaderNaviDropDown",pageCategory:window.digitalData.page.category.pageType,productMktName:d.$secondEle.find(".product-link__active").data("title"),buttonName:"drop down button"}))
})
}},bindNavToggle:function(){var f=document.getElementById("header-v4");
var d=document.getElementById("header-placeholder");
var i=document.getElementById("second-navigation-v4");
var j=navigator.userAgent;
var e=j.indexOf("compatible")>-1&&j.indexOf("MSIE")>-1;
var k=!!window.ActiveXObject?!!window.ActiveXObject:"ActiveXObject" in window;
var h=j.indexOf("Edge")>-1;
if(i&&f){if($(".mkt-ad-banner").length>0){$(".mkt-ad-banner").after(i)
}else{$("#header-v4").after(i)
}if(!(Granite&&Granite.author)){f.classList.add("minisite-nav");
b.pageTypeNavFlag=true
}var l=(function(){var n=document.createElement("a"),m=n.style;
m.cssText="position:sticky;position:-webkit-sticky";
return m.position.indexOf("sticky")!==-1
})();
if(l==false||e||k||h){document.body.classList.add("no-sticky");
var g=f.clientHeight;
if(h){i.classList.add("isEdge")
}window.onscroll=function(){if(window.pageYOffset>g){d.style.paddingTop=i.clientHeight+"px";
i.classList.add("stuck")
}else{i.classList.remove("stuck");
d.style.paddingTop=0
}};
window.onresize=function(){g=f.clientHeight
}
}}}};
var c={init:function(){var d=this;
if(window.innerWidth<d.uiBoundaryVal&&window.window.pageCategory=="support"){$(".nav-addons .nav-toggle").click(function(){$($(".main-nav .is-support-menu").find("a")[0]).click()
})
}$(".show-logout .login-extra-item-html").html(d.renderLoginItems(true));
$(".show-login .login-extra-item-html").html(d.renderLoginItems(false));
if(window.isECommerceSite==="None"){$("body").addClass("none-ecommerce")
}},renderLoginItems:function(j){var f=$("#login-extra-item").val();
if(!f){return
}var h="";
var e=JSON.parse(f);
if(j){var d=e.filter(function(i){return i.url.indexOf("order")>-1
});
if(d.length>0){d[0].url=window.dialogLinkHandler($("#ec-url-orderListLink").val());
d[0].text=ecCom.I18n.get("ec_my_order")
}}for(var g=0;
g<e.length;
++g){h+='<li class="login-other-items main-nav__item"><a href="'+window.dialogLinkHandler(e[g].url)+'" title="'+e[g].text+'" target="'+(e[g].openNewPage?"_blank":"_self")+'" class="a-support-common dmpa-click-dispach" cat="pop_up_account" act="click_on_'+e[g].text+'" lab="${item.text}"><img class="left-icon"'+(e[g].iconPath?'src="'+e[g].iconPath+'" alt="icon" ':"")+' style="width:24px; height: 24px;display: none;'+(e[g].iconPath?"":"visibility: hidden;")+'"><span>'+e[g].text+"</span></a>"+(e[g].rightIcon?'<img class="right-icon" src="'+e[g].rightIcon+'" alt="icon"/>':"")+"</li>"
}return h
}};
$(function(){b.init();
a.init();
c.init()
});
$(window).on("load resize",function(){b.calcMainNavWidth();
b.customScrollBarProducts();
b.bindIpJump()
})
}());
(function(){var a={$selector:$(".n02-expanded-products"),navVersion:$("#header-v4 #mainNav").val()||"nav-v1",uiBoundaryVal:1200,init:function(){var b=this;
b.uiBoundaryVal=b.navVersion=="nav-v1"?1200:1366;
if(b.$selector.length){b.imageDimension()
}$(window).on("load",function(){setTimeout(function(){b.imageDimension()
},100)
});
$(window).on("resize",function(){b.imageDimension()
})
},imageDimension:function(){var b=this;
if($(window).width()>b.uiBoundaryVal){b.$selector.each(function(){var e=$(this).find(".dropdown__holder--two-img");
var d=$(this).find(".dropdown__holder--four-img");
if(e.length&&d.length){var c=d.css("padding-top");
var g=$(this).find(".dropdown__four-images .dropdown__right-col").height();
var f=c+g;
$(this).find(".dropdown__holder--two-img").css("padding-bottom",f)
}})
}if($(window).width()>=b.uiBoundaryVal){b.mobileServicesbg(".one-two-icon .pc-bg")
}},mobileServicesbg:function(b){$(b).each(function(d,e){var c=$(this).attr("pc-bg");
$(this).attr("style","background-image: url("+c+")")
})
}};
$(function(){a.init()
});
$(document).on("click",".dropdown__block-item",function(){var b=$(this).data("mobileservice"),d=$(this).attr("href"),e=CBG_SITE_ROOT.substring(0,CBG_SITE_ROOT.length-1)+""+window.location.pathname,c=window.digitalData.page.category.pageType==="homepage"?"homepage":window.location.pathname.split(siteCode)[1];
var f={category:"navigation interaction",label:b,value:d,location:e,uri:c,subModuleName:"Marketing"};
if(typeof dmpa5!=="undefined"){dmpa5("trackEvent","click",f)
}});
$(document).on("click",".dropdown__big-link",function(){var f=$(this).attr("title"),c=$(this).attr("href"),d=CBG_SITE_ROOT.substring(0,CBG_SITE_ROOT.length-1)+""+window.location.pathname,b=window.digitalData.page.category.pageType==="homepage"?"homepage":window.location.pathname.split(siteCode)[1];
var e={category:"navigation interaction",label:f,value:c,location:d,uri:b};
if(typeof dmpa5!=="undefined"){dmpa5("trackEvent","click",e)
}})
}());
(function(){var a={$selector:$(".n03-expanded-support"),$content:$(".js-item-content"),$link:$(".js-support-link"),activeClass:"dropdown__big-link--active",visibleClass:"dropdown__row--visible",init:function(){if(this.$selector.length){this.supportNav()
}},supportNav:function(){var b=this;
this.$link.on("click",function(d){var c=$(this).parent().index();
b.$link.removeClass(b.activeClass);
$(this).addClass(b.activeClass);
b.$content.removeClass(b.visibleClass);
b.$content.eq(c).addClass(b.visibleClass);
d.preventDefault()
})
}};
$(function(){a.init()
})
}());
(function(){var a={$selector:$(".n12-search"),$searchContainer:$(".search__form-container"),$searchInput:$(".js-search-autocomplete"),$btnClearSearch:$(".js-search-clear"),$popularWrap:$(".popular-show-wrap"),$popularProduct:$(".popular-product .dropdown__row-mobile"),searchFormAutocompleteVisibleClass:"search__form-container--autocomplete-visible",hotSearchTxt:$(".n12-search #headerHotSearchText").val()||"",canSearch:false,keywords:"",phCanSearch:$(".js-search-autocomplete").data("enable-ph-search")||"no",phVal:$(".js-search-autocomplete").attr("placeholder"),scheme:window.location.protocol+"//",domain:window.location.host+"/",supportApiUrl:supportv2.supportApiUrl,pageInfo:window.digitalData.page.pageInfo,popularData:[],lazyInitFlag:true,init:function(){if(this.$selector.length){this.lazyInit();
this.clearSearch();
this.customScrollBarProducts();
this.handleSearchSubmit()
}},lazyInit:function(){var b=this;
$(".js-open-search").click(function(){if(b.lazyInitFlag){b.getSearchStatus();
b.lazyInitFlag=false;
b.getJson()
}})
},optimizeSearchLink:function(){var b=$(".n12-search.popup").find(".dropdown__series-link");
b.on("focus",function(){$(this).children(".dropdown__holder").length>0&&$(this).children(".dropdown__holder").addClass("h-focus-active")
});
b.on("blur",function(){$(this).children(".dropdown__holder").length>0&&$(this).children(".dropdown__holder").removeClass("h-focus-active")
})
},initPopularSearch:function(){var e=this;
e.$searchContainer.addClass(e.searchFormAutocompleteVisibleClass);
e.optimizeSearchLink();
e.$popularWrap.addClass(e.searchFormAutocompleteVisibleClass);
var c=$(".easy-autocomplete-container ul");
var d='<div class="eac-category">'+$(".popular-text").attr("data-value")+"</div>";
var b="";
$.each(e.popularData,function(g,f){if(window.location.href.indexOf("/support")>0){b+='<li><div class="eac-item"><a href=\''+e.scheme+e.domain+e.pageInfo.siteCode2+"/search/?keyword="+encodeURIComponent(f)+"&tag=support'>"+f+"</a></div></li>"
}else{b+='<li><div class="eac-item"><a href=\''+e.scheme+e.domain+e.pageInfo.siteCode2+"/search/?keyword="+encodeURIComponent(f)+"'>"+f+"</a></div></li>"
}});
c.empty().append(d).append(b).show()
},getJson:function(){var b=this;
$.ajax({url:b.scheme+b.domain+b.pageInfo.siteCode2+"/_jcr_content.allProducts.json",success:function(c){b.initSearchAutocomplete({suggested:c.allProduct.split(",")});
b.initEachProduct(c.recommendedProduct.split(","))
}});
if(typeof sgwHost=="undefined"||sgwHost==null||sgwHost==""){$.ajax({url:b.supportApiUrl+"/services/service/vofficial/hot",type:"GET",data:{qAppName:"HuaweiOfficial",site:b.pageInfo.siteCode2.toUpperCase(),language:b.pageInfo.language?b.pageInfo.language.replace("_","-"):""},dataType:"jsonp",jsonp:"jsonp",success:function(d){for(var c in d){b.popularData.push(d[c].key)
}}})
}else{$.ajax({type:"GET",url:sgwHost+"/cmkt/venus/hot/1",dataType:"json",jsonp:"json",contentType:"application/json",data:{appName:"HuaweiOfficial",language:window.digitalData.page.pageInfo.siteCode2.toUpperCase()},beforeSend:function(c){c.setRequestHeader("SGW-APP-ID",sgwAppId)
},success:function(c){if(c.result&&c.result.length>0){var e=c.result;
for(var d in e){b.popularData.push(e[d].key)
}}}})
}},initEachProduct:function(b){var c=this;
$.each(b,function(e,f){if(e<3){var d=f.replace(/\|\|/,"|").split("|");
c.$popularProduct.append('<div class="list dropdown__right-col col-xl-4 col-xs-6"><a class="dropdown__series-link" href="'+d[2].replace("/content/huawei-cbg-site","")+'"><div class="dropdown__holder"><img class="dropdown__image-centered" src="'+d[1]+'"/></div></a><div><a class="heading dropdown__series-link" href="'+d[2].replace("/content/huawei-cbg-site","")+'">'+d[0]+"</a></div></div>")
}})
},initSearchAutocomplete:function(b){var c=b.length;
if(this.$searchInput.length){var d=this;
this.$searchInput.easyAutocomplete({data:b,template:{type:"custom",method:function(f,e){return"<a href='"+d.scheme+d.domain+d.pageInfo.siteCode2+"/search/?keyword="+encodeURIComponent(e)+"'>"+f+"</a>"
}},categories:[{listLocation:"suggested",header:$(".suggested-text").attr("data-value"),maxNumberOfElements:10}],list:{maxNumberOfElements:10,match:{enabled:true},onShowListEvent:function(){d.$searchContainer.addClass(d.searchFormAutocompleteVisibleClass);
d.$popularWrap.addClass(d.searchFormAutocompleteVisibleClass);
d.optimizeSearchLink();
if(d.$searchInput.val().trim().length<1&&d.$searchInput.is(":focus")){d.initPopularSearch()
}},onHideListEvent:function(){d.$searchContainer.removeClass(d.searchFormAutocompleteVisibleClass);
d.$popularWrap.removeClass(d.searchFormAutocompleteVisibleClass);
if(d.$searchInput.val().trim().length<1&&d.$searchInput.is(":focus")){d.initPopularSearch()
}}}});
if($.isIos()){this.$searchInput.click(function(){if(d.$searchInput.val().trim().length<1&&d.$searchInput.is(":focus")){d.initPopularSearch();
d.handleSearchSubmit()
}})
}else{this.$searchInput.focus(function(){if(d.$searchInput.val().trim().length<1&&d.$searchInput.is(":focus")){d.initPopularSearch();
d.handleSearchSubmit()
}})
}}},getSearchStatus:function(){var c=this;
var b=c.$searchInput.val().trim();
if(c.phCanSearch=="yes"&&c.phVal&&b.length==0){c.canSearch=true;
c.keywords=c.phVal
}else{if(b.length>1){c.canSearch=true;
c.keywords=b
}else{c.canSearch=false
}}if(c.canSearch){$(".v4.n12-search .search__form-submit").addClass("active")
}else{$(".v4.n12-search .search__form-submit").removeClass("active")
}},handleSearchSubmit:function(){var b=this;
$(".search__form-submit").on("click",function(){b.getSearchStatus();
if(b.canSearch){if(window.location.href.indexOf("/support")>0){window.location.href=b.scheme+b.domain+b.pageInfo.siteCode2+"/search/?keyword="+encodeURIComponent(b.keywords)+"&tag=support"
}else{window.location.href=b.scheme+b.domain+b.pageInfo.siteCode2+"/search/?keyword="+encodeURIComponent(b.keywords)
}}else{$(".n12-search .search_toast").fadeIn().delay(2000).fadeOut()
}});
b.$searchInput.keyup(function(c){b.getSearchStatus();
if(c.keyCode=="13"){if(b.canSearch){if(window.location.href.indexOf("/support")>0){window.location.href=b.scheme+b.domain+b.pageInfo.siteCode2+"/search/?keyword="+encodeURIComponent(b.keywords)+"&tag=support"
}else{window.location.href=b.scheme+b.domain+b.pageInfo.siteCode2+"/search/?keyword="+encodeURIComponent(b.keywords)
}}else{$(".n12-search .search_toast").fadeIn().delay(2000).fadeOut()
}}})
},customScrollBarProducts:function(){if(window.innerWidth>1199.98){$(".v4.n12-search").mCustomScrollbar({axis:"y",scrollbarPosition:"outside"})
}else{$(".v4.n12-search").mCustomScrollbar("destroy")
}},clearSearch:function(){var b=this;
b.$btnClearSearch.on("click",function(){b.$searchInput.val("")
})
}};
$(function(){a.init()
})
}());
(function(){var a={$selector:$(".n09-footer"),$scrollTopBtn:$(".js-scroll-top"),uspList:".usp-list",$footerAccordionBtn:$(".js-footer-accordion-btn"),$lanChangeSelector:$(".language-switcher"),init:function(){if(this.$selector.length){this.bindScrollTopClick();
this.footerAccordionLinks();
this.initUspListSlider();
this.footerTelInit();
this.bindSiteChangeClick();
this.lazyLoadImg();
var b=this;
$(window).on("scroll",function(){b.lazyLoadImg()
});
$(window).on("resize",function(){b.initUspListSlider()
})
}},bindScrollTopClick:function(){this.$scrollTopBtn.on("click",function(){$("html, body").animate({scrollTop:0},600)
})
},initUspListSlider:function(){var b=this;
if($(window).width()<720&&$(this.uspList)&&!$(this.uspList).hasClass("swiper-container-initialized")&&$(".usp-list__container .usp-list__item").length>1){$(".n09-footer .swiper-next,.n09-footer .swiper-prev").show();
new Swiper(b.uspList,{speed:600,loop:true,pagination:{el:".usp-list .swiper-pagination"},navigation:{nextEl:".n09-footer .swiper-next",prevEl:".n09-footer .swiper-prev"}})
}else{$(".n09-footer .swiper-next,.n09-footer .swiper-prev").hide()
}},footerAccordionLinks:function(){if($(window).width()<992){$(".footer-links__title.js-footer-accordion-btn").attr("tabindex",0);
function b(c){c.toggleClass("footer-links__title--active");
c.siblings(".footer-links__list").stop().slideToggle(300);
if(c.hasClass("footer-links__title--active")){c.attr("aria-expanded",true)
}else{c.attr("aria-expanded",false)
}}this.$footerAccordionBtn.on("keydown",function(c){if(c.keyCode===13){b($(this))
}});
this.$footerAccordionBtn.on("click",function(){b($(this))
})
}},footerTelInit:function(){if($(window).width()<768){$(".phone-icon").each(function(b,c){var f=$(c).text().replace(/\s*/g,"");
var e=$(c).text();
var d="<a data-clicktocall='footer_center' href='tel:"+f+"'>"+e+"</a>";
$(c).html(d)
})
}},bindSiteChangeClick:function(){this.$lanChangeSelector.find("a").on("click",function(){var b=window.location.pathname.split("/");
if(b&&b.length>1){sessionStorage.setItem("origin_site_path",b[1])
}var c={event:"footerCountrySwitch",clickName:"country switch_enter",clickType:"action"};
window.dataLayer.push(addATCommonFields(c))
})
},lazyLoadImg:function(){this.$selector.find(".lazyload-target:in-viewport").each(function(){var b=$(this);
b.find(".lazyload-img").each(function(){var c=$(this);
if(c.is("img")){c.attr("src",c.attr("data-src"));
b.removeClass("lazyload-target")
}else{if(c.is("source")){c.attr("srcset",c.attr("data-srcset"));
b.removeClass("lazyload-target")
}}})
})
}};
$(function(){a.init()
})
}());
var login_leave=null;
$(function(){$(".huawei-v4 .login-v4-wrap .login-v4 .signInBtn.a-sup-common").on("click",function(){window.location.href=getLoginUri()
});
$(".huawei-v4 .login-v4-wrap .login-v4 .a-sup-common.registeredBtn").on("click",function(){window.location.href=getRegisterUrl($(".huawei-v4 .login-v4-wrap ul.show-login").attr("data-register-type"))
});
if(isLogin()){$(".huawei-v4 .login-v4-wrap").addClass("signin");
$(".huawei-v4 .login-v4-wrap .app-sign-user .signin-user").text($.cookie("user"));
$(".huawei-v4 .login-v4-wrap .login-v4 .logout-btn .a-sup-common.my-exit").on("click",function(){webLogout();
if(typeof asyncUumLogout==="function"){asyncUumLogout()
}var b=$(".huawei-v4 .login-v4-wrap .login-v4 .login-v4-cnt .show-login").attr("data-support-url");
var a="";
var c="";
try{a=loginApiUrl.cmscApiUrl;
c=loginApiUrl.huaweitimeApiUrl
}catch(d){}if(typeof huaweitimeLogout==="function"&&typeof cmscLogout==="function"){if(c!=null&&c!=""){if(a!=null&&a!=""){huaweitimeLogout(cmscLogout(function(){window.location.href=getWebsiteLogoutUrl(b)
}))
}else{huaweitimeLogout(function(){window.location.href=getWebsiteLogoutUrl(b)
})
}}else{if(a!=null&&a!=""){cmscLogout(function(){window.location.href=getWebsiteLogoutUrl(b)
})
}else{window.location.href=getWebsiteLogoutUrl(b)
}}}else{window.location.href=getWebsiteLogoutUrl(b)
}});
if($(window).width()>1199.98){$(".huawei-v4 .login-v4-wrap.signin a.login-v4-but").click(function(a){a.stopPropagation();
window.location.href=$(".huawei-v4 .login-v4-wrap .login-v4 .login-v4-cnt .show-login").attr("data-support-usercenter-url")
})
}}else{$(".huawei-v4 .login-v4-wrap").removeClass("signin")
}});
function loginBeforeAccountCenter(a){window.getUPLoginUrl(a).then(function(b){if(!ecCom.isPC){window.open(b.loginWapUrl,"_self")
}else{window.open(b.loginWebUrl,"_self")
}})
}var CBG_SITE_ROOT="/content/huawei-cbg-site/";
var CBG_SITE_EDITOR_ROOT="/editor.html/content/huawei-cbg-site/";
(function(){var p="EN";
var e="LEVANT";
var n="LATIN";
var t=$(".header");
var h=$("#header-placeholder");
var m=$(".header .n01-main-navigation");
var j=m.find(".main-nav");
var f=m.find(".popup");
var s=$(".header .n12-search");
var c=$(".header .login-v4");
var i=$(".header #mainNav").val()||"nav-v1";
var a=i=="nav-v1"?1200:1366;
function d(){var v=mktConfig.sgwApi;
var w="";
if(v){w=v+"/cmkt/webapi/location/1"
}else{var u=(location.href.indexOf(".test.huawei.com")==-1&&location.href.indexOf("localhost")==-1)?"https://consumer.huawei.com/cmkt":supportv2.cmktApiUrl;
w=u+"/services/service/webapi/location"
}return w
}$(document).ready(function(){if(window.integrationJsInterface||window.integrationJsInterfaceWebview){return
}if($(".ip-jump-wrap").length==0){return
}if($.cookie("checkRegion")){return
}if(location.href.indexOf("/en/worldwide")!=-1){return
}$.ajax({type:"POST",url:d(),dataType:"json",contentType:"application/json",beforeSend:function(u){if(mktConfig.sgwApi){u.setRequestHeader("SGW-APP-ID",sgwAppId)
}},data:{},success:function(u){if(u.returnCode==0&&u.country&&window.digitalData.page.pageInfo.countryCode!=u.country){if(b(u.country)){q(u.country)
}}}})
});
var o=[{code:"UK",path:"uk",siteName:"United Kingdom",message:"You are visiting a website that is different from your current country or region, would you like to switch to your local site?",buttonText:"Continue",selectText:"Other country or region"},{code:"GB",path:"uk",siteName:"United Kingdom",message:"You are visiting a website that is different from your current country or region, would you like to switch to your local site?",buttonText:"Continue",selectText:"Other country or region"},{code:"IE",path:"ie",siteName:"Ireland",message:"You are visiting a website that is different from your current country or region, would you like to switch to your local site?",buttonText:"Continue",selectText:"Other country or region"},{code:"IT",path:"it",siteName:"Italia",message:"La pagina che stai per visitare è diversa dal tuo Paese o Regione attuale. Vuoi passare al tuo sito locale?",buttonText:"Continua",selectText:"Seleziona altro Paese o Regione"},{code:"ES",path:"es",siteName:"España",message:"Estas visitando un sitio web diferente de su país o región actual, ¿te gustaría cambiar a la web local?",buttonText:"Continuar",selectText:"Seleccionar otro país o región"},{code:"FR",path:"fr",siteName:"France",message:"Vous visitez un site Web différent de votre pays ou région actuelle, souhaitez-vous passer à votre site local?",buttonText:"Continuer",selectText:"Autre pays/région"},{code:"DE",path:"de",siteName:"Deutschland",message:"Du besuchst eine Website, die sich von deinem derzeitigen Land oder deiner Region unterscheidet, möchtest du zu der passenden lokalen Website wechseln?",buttonText:"Fortfahren",selectText:"Anderes Land oder andere Region"},{code:"NL",path:"nl",siteName:"Nederland",message:"U bezoekt een website die niet overeenkomt met uw huidige land of regio, wilt u veranderen naar uw lokale site?",buttonText:"Ga verder",selectText:"Ander land of andere regio"},{code:"BE",path:"be",siteName:"België(Dutch)",message:"U bezoekt een website die niet overeenkomt met uw huidige land of regio, wilt u veranderen naar uw lokale site?",buttonText:"Ga verder",selectText:" Ander land of andere regio"},{code:"BE",path:"be-fr",siteName:"Belgique(French)",message:"Vous êtes sur un site qui ne correspond pas à votre propre pays ou région. Voulez-vous accéder à votre site local?",buttonText:" Continuer",selectText:"Autre pays ou région"},{code:"CH",path:"ch",siteName:"Schweiz(Deutsch)",message:"Du besuchst eine Website, die sich von deinem derzeitigen Land oder deiner Region unterscheidet, möchtest du zu der passenden lokalen Website wechseln?",buttonText:"Fortfahren",selectText:"Anderes Land oder andere Region"},{code:"CH",path:"ch-fr",siteName:"Suisse(Français)",message:"Vous visitez un site Web différent de votre pays ou région actuelle, souhaitez-vous passer à votre site local?",buttonText:"Continuer",selectText:"Autre pays/région"},{code:"PT",path:"pt",siteName:"Portugal",message:"Está num site diferente do seu país ou região atual, gostaria de mudar para o seu site local?",buttonText:"Continuar",selectText:"Outro país ou região"},{code:"AU",path:"au",siteName:"Australia",message:"You are visiting a website that is different from your current country or region, would you like to switch to your local site?",buttonText:"Continue",selectText:"Other country or region"}];
window.buildPromptRegion=q;
function q(v){var y=[];
for(var x=0;
x<o.length;
x++){if(o[x].code==v){y.push(o[x])
}}var u=k(v);
var w=window.digitalData.page.pageInfo.countryCode;
if(y.length==0){if(u==w){return
}if(w!=p){y.push({code:"EN",path:"en",siteName:"Worldwide",message:"You are visiting a store that is different to your current location,would you like to switch to your local store?",buttonText:"continue",selectText:"choose other region"})
}else{return
}}var z="";
z+='<span class="ipJump-close"></span>';
z+='<div class="ipJump-cnt">';
z+='<div class="ipJump-copywriting">'+y[0].message+"</div>";
z+='<div class="ipJump-bnt clearfix">';
z+='<div class="ipJump-select">';
z+='<span class="ipJump-select-title">'+y[0].siteName+"</span>";
z+='<ul class="clearfix">';
for(var x=0;
x<y.length;
x++){z+='<li path="'+y[x].path+'" siteName="'+y[x].siteName+'">'+y[x].siteName+"</li>"
}z+='<li class="other-region" path="en" siteName="'+y[0].selectText+'">'+y[0].selectText+"</li>";
z+="</ul>";
z+="</div>";
z+='<a class="ip-jump-go" href="javascript:;" message="'+y[0].message+'" buttonText="'+y[0].buttonText+'" path="'+y[0].path+'" title="'+y[0].buttonText+'" >'+y[0].buttonText+"</a>";
z+="</div>";
z+="</div>";
$(".ip-jump-wrap").html(z).show();
r();
$(".ipJump-select").off("click");
$(".ipJump-select").on("click",function(){if($(".ipJump-select ul").is(":visible")){$(this).removeClass("active")
}else{$(this).addClass("active")
}});
$(".ip-jump-wrap ul li").off("click");
$(".ip-jump-wrap ul li").on("click",function(){var A=$(this);
$(".ip-jump-wrap .ipJump-select-title").text(A.attr("siteName"));
$(".ip-jump-wrap .ip-jump-go").attr("path",A.attr("path"))
});
$(".ip-jump-wrap .ip-jump-go").off("click");
$(".ip-jump-wrap .ip-jump-go").on("click",function(){var B={event:"ipPop-up",buttonName:"go",countryCode:sysConfig.countryCode,clickName:"ip relocate_click go "+sysConfig.countryCode};
var A=null;
window.dataLayer.push(addATCommonFields(B));
if($(this).attr("path")=="en"){if(location.href.indexOf("/content/huawei-cbg-site/")!=-1){location.href=location.origin+"/content/huawei-cbg-site/en/worldwide.html";
A=location.origin+"/content/huawei-cbg-site/en/worldwide.html"
}else{location.href=location.origin+"/en/worldwide/";
A=location.origin+"/en/worldwide/"
}}else{l($(this).attr("path"));
A=$(this).attr("path")
}dmpaCommon("trackEvent","click","ip relocated pop-up interaction","go",A)
});
$(".ip-jump-wrap .ipJump-close").click(function(){var A={event:"ipPop-up",buttonName:"close",clickName:"ip relocate_click close "+sysConfig.countryCode,clickType:"navigation"};
window.dataLayer.push(addATCommonFields(A));
dmpaCommon("trackEvent","click","ip relocated pop-up interaction","close","");
$(".ip-jump-wrap").hide();
g();
r()
})
}function r(){var u=t.innerHeight();
var v=0;
if($("#locationSecret").is(":visible")){var w=$("#locationSecret").height();
t.css("top",w);
v=w+u
}else{t.toggleClass("hasIp");
$(".page-plp").toggleClass("hasIp");
$(".product-filter__inner--fixed").css("top",u);
v=u
}h.css({height:v});
s.css("top",v);
if(Mkt.Util.windowWidth()>=a&&!t.hasClass("mb-ui")){f.css("top",u)
}else{j.css("top",v);
c.css("top",v)
}}function l(v){var x=location.origin+"/"+v.toLowerCase()+"/";
var u=digitalData.page.pageInfo.siteCode2||"";
var w=location.pathname;
var y="";
if(w.indexOf(CBG_SITE_EDITOR_ROOT)==0){w=w.replace(CBG_SITE_EDITOR_ROOT,"")
}else{if(w.indexOf(CBG_SITE_ROOT)==0){w=w.replace(CBG_SITE_ROOT,"");
if(w.indexOf("/")>-1){y=location.origin+location.pathname.replace("/"+u+"/","/"+v.toLowerCase()+"/")
}else{y=location.origin+location.pathname.replace("/"+u+".html","/"+v.toLowerCase()+".html")
}}else{y=location.origin+location.pathname.replace("/"+u+"/","/"+v.toLowerCase()+"/")
}}$.ajax({type:"get",cache:false,url:y+location.search,dataType:"html",complete:function(z){if(z.status==404){location.href=x
}else{location.href=y+location.search
}}})
}function k(u){switch(u){case"LB":u="LEVANT";
break;
case"JO":u="LEVANT";
break;
case"IQ":u="LEVANT";
break;
case"GT":u="LATIN";
break;
case"DO":u="LATIN";
break;
case"UY":u="LATIN";
break;
case"EC":u="LATIN";
break;
case"BO":u="LATIN";
break;
case"HN":u="LATIN";
break;
case"PY":u="LATIN";
break;
case"VE":u="LATIN";
break;
case"CR":u="LATIN";
break;
case"SV":u="LATIN";
break;
case"NI":u="LATIN";
break;
case"jM":u="LATIN";
break;
default:break
}return u
}function g(u){$.cookie("checkRegion","true",{path:"/",expires:7})
}function b(u){var v=["UK","GB","IT","ES","FR","DE","NL","BE","CH","IE","PT","AU"];
return v.indexOf(u)>-1
}}());
(function(a){a.Constants=(function(){var b={};
b.SITE_ROOT_PATH="/content/huawei-cbg-site/";
return b
}())
}(Mkt));
(function(a,b){b.Util=(function(){var e=b.Constants.SITE_ROOT_PATH;
var d="/";
var f=".html";
var c={};
c.isEditMode=location.href.indexOf("/editor.html/")!=-1;
c.isDispatcher=location.pathname.indexOf(e)==-1;
c.isIE=!!window.ActiveXObject||"ActiveXObject" in window;
c.isAppWebview=window.integrationJsInterface||window.integrationJsInterfaceWebview;
c.callAEMServletBySelector=function(h,i,l){var j=a.Deferred();
var g={};
var k=window.location.origin+h;
a.ajax(k,{async:i,dataType:"json",data:l,success:function(m){j.resolve(m)
},error:function(n){var m={};
m.message="Call AEM servlet fail, please check the servlet detail";
m.servletDetail=n.responseText;
j.reject(m)
}});
return j.promise()
};
c.isEmpty=function(g){if(!a.isEmptyObject(g)&&g!=""){return false
}else{return true
}};
c.isNotEmpty=function(g){return !c.isEmpty(g)
};
c.trim=function(g){if(typeof g=="undefined"||g==null){return""
}else{return(""+g).trim()
}};
c.setCookie=function(i,m,j,k,h,g,l){j=j||".huawei.com";
k=k||"/";
h=h||0;
g=g||0;
l=l||0;
if(h===0&&g===0&&l===0){window.document.cookie=i+"="+m+";domain="+j+";path="+k
}else{let exp=new Date();
let allTime=(h*24+g)*60+l;
exp.setTime(exp.getTime()+allTime*60*1000);
window.document.cookie=i+"="+m+";domain="+j+";path="+k+";expires="+exp.toGMTString()
}};
c.getCookie=function(h){var g,i=new RegExp("(^| )"+h+"=([^;]*)(;|$)");
if(g=document.cookie.match(i)){return g[2]
}else{return null
}};
c.clearCookie=function(g,h){var i=new Date();
i.setTime(i.getTime()-(24*60*60*1000));
window.document.cookie=g+"= ;expires="+i.toGMTString()+";domain="+h+";path=/"
};
c.pageWidth=function(){return document.body.scrollWidth
};
c.pageHeight=function(){return document.body.scrollHeight
};
c.windowWidth=function(){var g=document.documentElement;
return window.innerWidth||(g&&g.clientWidth)||document.body.clientWidth
};
c.windowHeight=function(){var g=document.documentElement;
return window.innerHeight||(g&&g.clientHeight)||document.body.clientHeight
};
c.scrollX=function(){var g=document.documentElement;
return window.pageXOffset||(g&&g.scrollLeft)||document.body.scrollLeft
};
c.scrollY=function(){var g=document.documentElement;
return window.pageYOffset||(g&&g.scrollTop)||document.body.scrollTop
};
c.endBrowser=function(){var g=navigator.userAgent;
var h=navigator.appVersion;
return{trident:g.indexOf("Trident")>-1,presto:g.indexOf("Presto")>-1,webKit:g.indexOf("AppleWebKit")>-1,gecko:g.indexOf("Gecko")>-1&&g.indexOf("KHTML")==-1,mobile:!!g.match(/AppleWebKit.*Mobile.*/),ios:!!g.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/),android:g.indexOf("Android")>-1||g.indexOf("Linux")>-1,iPhone:g.indexOf("iPhone")>-1,iPad:g.indexOf("iPad")>-1,webApp:g.indexOf("Safari")==-1,weixin:g.indexOf("MicroMessenger")>-1,qq:g.match(/\sQQ/i)==" qq"}
};
c.isMobileEnd=function(){return c.endBrowser().mobile||c.endBrowser().android||c.endBrowser().ios
};
c.stopBubble=function(g){if(g&&g.stopPropagation){g.stopPropagation()
}else{window.event.cancelBubble=true
}};
c.stopDefault=function(g){if(g&&g.preventDefault){g.preventDefault()
}else{window.event.returnValue=false
}return false
};
c.dataURLtoFile=function(i){var g=i.split(",");
var l=g[0].match(/:(.*?);/)[1];
var h=atob(g[1]);
var j=h.length;
var k=new Uint8Array(j);
var m=new Date().getTime()+".png";
while(j--){k[j]=h.charCodeAt(j)
}return new File([k],m,{type:l})
};
c.getRequest=function(){var h=location.search;
var g=new Object();
if(h.indexOf("?")!=-1){var l=h.substr(1);
var k=l.split("&");
for(var j=0;
j<k.length;
j++){g[k[j].split("=")[0]]=decodeURI(k[j].split("=")[1])
}}return g
};
c.getCurrPageUrl=function(){return window.location.protocol+"//"+window.location.host
};
c.checkEmail=function(g){var i=false;
var h=/^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z]{2,4}$/;
if(h.test(g)){i=true
}else{i=false
}return i
};
c.emailHide=function(h){if(c.isEmpty(h)){return""
}var i=h.split("@");
if(i[0].length>1){var k=parseInt(i[0].length/2);
var j=new RegExp(".","g");
var l=i[0].replace(j,"*");
var g=i[0].substring(0,k)+l.substring(k,i[0].length);
return g+"@"+i[1]
}else{return"*@"+i[1]
}};
return c
}())
}(jQuery,Mkt));
(function(a,b){b.I18n=(function(){var e={};
var j={};
var c="/libs/cq/website/i18n";
var d=600000;
var g="mkt_i18n_";
var f=g+"expired_";
var i=false;
e.init=function(){var k=new Date().getTime();
var m=sessionStorage.getItem(f+e.getLocale());
if(m==null||m==""){h()
}else{if(k>=m){sessionStorage.removeItem(g+e.getLocale())
}}var l=sessionStorage.getItem(g+e.getLocale());
j=l?JSON.parse(l):{};
if(a.isEmptyObject(j)){e.initDictionary()
}};
e.initDictionary=function(){c=c+"."+e.getLocale()+".json";
b.Util.callAEMServletBySelector(c,false).done(function(k){sessionStorage.setItem(g+e.getLocale(),JSON.stringify(k));
j=k;
h()
})
};
e.get=function(l,k){if(!e.isInit){e.init();
e.isInit=true
}var m=j[l];
if(!m){m=l
}return e.patchText(m,k)
};
e.getLocale=function(){return window.digitalData.page.pageInfo.language
};
e.patchText=function(m,l){if(l||l=="0"){if(Array.isArray(l)){for(var k=0;
k<l.length;
k++){m=m.replace("{"+k+"}",l[k])
}}else{m=m.replace("{0}",l)
}}return m
};
var h=function(){var k=new Date(new Date().getTime()+d);
sessionStorage.setItem(f+e.getLocale(),k.getTime())
};
return e
}())
}(jQuery,Mkt));
var browser=getExplorerInfo();
var device=$(window).width()<1024?"mobile":"pc";
if(browser.type=="IE"||browser.type=="Edge"){device=$(window).width()<1007?"mobile":"pc"
}var PlpI18n={i18n_Buy:"",i18n_LearnMore:"",i18n_NoPrice:"",i18n_from:""};
if(window.isECommerceSite&&window.isECommerceSite!="None"){PlpI18n.i18n_Buy=ecCom.I18n.get("ec_buy");
PlpI18n.i18n_LearnMore=ecCom.I18n.get("ec_learn_more");
PlpI18n.i18n_NoPrice=ecCom.I18n.get("ec_no_price");
PlpI18n.i18n_from=ecCom.I18n.get("ec_from")
}function init_plpPrice(g,a,l,c){var d=g;
var h={},f="",k="";
if(c==="plp_banner"){f=d.parents(".product-listing-hero__container");
k=f.find(".product-listing-hero__buttons a.global-buy-button")
}else{if(c==="plp_productList"){f=d.parents(".product-col .product-block");
k=f.find(".product-block__details button")
}else{if(c==="compare"){f=d.parents(".hero-compare__product");
k=f.find(".hero-compare__links a.product_buy_btn")
}else{if(c==="pdp_relate"){f=d.parents(".relate-product-main .product-li");
k=f.find(".buy-common-btn button")
}else{if(c==="series_design"){f=d.parents(".series-main .series-product .series-product-list");
k=f.find(".btn-container a.series-btn1")
}}}}}f.addClass("ecCommerce");
var b=k.attr("data-enableec"),e=d.attr("data-colorname")?d.attr("data-colorname"):"",i=k.attr("data-ecpid");
if(i&&b=="true"&&a.minPriceByColors&&i==a.productId){if(a.minPriceByColors&&a.minPriceByColors.length>0){var j;
a.minPriceByColors.some(function(m){j=Mkt.Util.trim(m.color)==Mkt.Util.trim(e);
return j
});
$.each(a.minPriceByColors,function(o,m){var n=m.installmentInfos;
if(j){if(Mkt.Util.trim(e)==Mkt.Util.trim(m.color)){if(n&&n.length>0){h.hasStaging=n.sort(function(q,p){return p.num-q.num
})[0]
}h.minUnitPrice=m.unitPrice;
h.minOrderPrice=m.orderPrice
}}else{if(n&&n.length>0){if(a.installmentInfos&&a.installmentInfos.length>0){h.hasStaging=a.installmentInfos.sort(function(q,p){return p.num-q.num
})[0]
}}h.minUnitPrice=a.minUnitPrice;
h.minOrderPrice=a.minOrderPrice
}})
}price_show(f,h,a,l,c,k)
}}function price_show(q,l,s,p,o,d){var i="";
var f="";
var h=showFrom&&d.data("onepricedisplay")!==true;
var b=h?'<span class="text-from"> '+PlpI18n.i18n_from+" </span>":"";
if(h){if(putFromFront){i=b
}else{f=b
}}var g={};
if(l&&s){g.minOrderPrice=l.minOrderPrice?l.minOrderPrice:s.minOrderPrice;
g.minUnitPrice=l.minUnitPrice?l.minUnitPrice:s.minUnitPrice
}else{g.minOrderPrice=currentRes.minOrderPrice;
g.minUnitPrice=currentRes.minUnitPrice
}var c=enableInstallmentCfg&&(installmentDispType===""||installmentDispType==="noDisplay");
if(p&&!c){if(l){g.hasStaging=l.hasStaging?l.hasStaging:hasStaging
}else{g.hasStaging=hasStaging
}var n=window.innerWidth>=1024?"PC":"mobile",j="",k="";
if(enableInstallmentCfg){k=window.ecInstallmentInfo(l.hasStaging)
}else{if(window.siteCode==="uk"||window.siteCode==="de"||window.siteCode==="es"){j=ecCom.I18n.get("ec_finance_available")
}else{if(window.siteCode==="ru"){j=ecCom.I18n.get("ec_payment_in_installments",[g.hasStaging.amount])
}else{if(window.siteCode==="ro"){j=ecCom.I18n.get("ec_bank_installment")
}else{j=ecCom.I18n.get("ec_payment_in_installments",[g.hasStaging.num])
}}}k=ecCom.I18n.get("ec_installment_or")+" "+j
}var r="";
var m="";
if(enableRRP){r="<span>"+RRPText+"</span>";
m="text-decoration:none;"
}var a=g.minUnitPrice!=g.minOrderPrice?'<b class="plp-item-price"><ul class="proPrice"><li class="salePrice">'+i+"<span >"+window.ecCurrency(g.minUnitPrice)+" </span>"+f+'</li><li class="minorderprice" style='+m+">"+r+'<span class="plp-item-minorderprice">'+window.ecCurrency(g.minOrderPrice)+'</span></li><li class="amountPrice"><span >'+k+"</span></li></ul></b>":'<b class="plp-item-price"><ul class="proPrice"><li class="salePrice">'+i+"<span >"+window.ecCurrency(g.minUnitPrice)+" </span>"+f+'</li><li class="amountPrice"><span >'+k+"</span></li></ul></b>"
}else{var r="";
if(enableRRP){r='<span style="color: #bebebe;font-size: 13px;font-weight: normal;">'+RRPText+"</span>"
}a=g.minUnitPrice!=g.minOrderPrice?'<b class="plp-item-price"><ul class="proPrice"><div class="inShow"><li class="salePrice">'+i+"<span >"+window.ecCurrency(g.minUnitPrice)+"</span>"+f+'</li><li class="minorderPrice" >'+r+'<span class="plp-item-minorderprice">'+window.ecCurrency(g.minOrderPrice)+"</span></li></div></ul></b>":'<b class="plp-item-price"><ul class="proPrice"><div class="inShow"><li class="minorderPrice" ><span ></span></li><li class="salePrice">'+i+"<span >"+window.ecCurrency(g.minUnitPrice)+"</span>"+f+"</li></div></ul></b>"
}if(q){q.find(".plp-item-fromprice").html(a)
}$(".plp-item-fromprice").matchHeight({byRow:true})
}var ec_pageLoading_start=function(){var a='<div id="ec_page_loading" class="ec_page_loading"><i class="hsvg60 hsvg-load-ani"></i></div>';
if($("#ec_page_loading").length>0){$("#ec_page_loading").remove()
}$("body").css({"overflow-y":"hidden"});
$("body").append(a)
};
var ec_pageLoading_end=function(){$("#ec_page_loading").remove();
$("body").css({"overflow-y":"auto"})
};
function loadEcData(a,c,b){var d=[];
d=a.filter(function(e){return e&&e.trim()
});
setComponentButtonText(b);
if(d.length!=0){getMinPriceAndInv(d).then(function(v){if(v.resultCode===0){var u=v.data.minPriceAndInvList;
var r=new Map();
var j=[],s,h={},n={},f=new Map();
if(u){$.each(u,function(x){r.set(u[x].productId+"",u[x]);
j=u[x].installmentInfos;
if(j&&j.length>0){$.each(j,function(){f.set(u[x].productId+"",u[x].installmentInfos)
})
}else{console.log(u[x].productId+" ID产品  不存在  分期信息或超出分期限额")
}})
}var p={};
for(var q=0;
q<a.length;
q++){if(q==0){p=c
}else{p=p.next()
}var e="",t="",w="";
if(p.length==0){continue
}if(b==="plp_productList"){e=p.find(".product-block__details button");
p.addClass("plp-li-scrollShow")
}else{if(b==="plp_banner"){e=p.find(".product-listing-hero__buttons a.global-buy-button")
}else{if(b==="compare"){e=p.find(".hero-compare__links a.product_buy_btn")
}else{if(b==="pdp_relate"){e=p.find(".buy-common-btn button")
}else{if(b==="series_design"){e=p.find(".btn-container a.series-btn1")
}}}}}t=e.attr("data-ecpid");
w=e.attr("data-enableec");
var o=r.get(t),m=f.get(t);
var g="";
if(t&&m){h.amount=Math.min.apply(Math,m.map(function(i){return i.amount
}));
n=m.sort(function(x,i){return i.num-x.num
})[0]
}if(w=="true"&&t&&o){if(o.hasInv&&o.minUnitPrice){var k=o,l=m;
if(b==="plp_productList"){$.each($(".product-row .swatches__item").find("button"),function(z,y){var A=o,x=m;
$(y).click(function(){init_plpPrice($(this),A,x,b)
})
});
$.each($(".product-wrap .swatches .swatches__wrapper"),function(y,x){var z=o,i=m;
init_plpPrice($(x).find("div").first().find("button"),z,i,b)
});
if($(".product-block__details").length>0&&device=="mobile"){$.each($(".product-block__details"),function(y,x){var z=o,i=m;
init_plpPrice($(x),z,i,b)
})
}}else{if(b==="plp_banner"){if($(".product-listing-hero__container .swatches__item").length>0){$.each($(".product-listing-hero__container .swatches__item"),function(z,y){var A=o,x=m;
$(y).click(function(){init_plpPrice($(this),A,x,b)
})
});
$.each($(".product-listing-hero__container .swatches .swatches__wrapper"),function(y,x){var z=o,i=m;
init_plpPrice($(x).find("div").first().find("button"),z,i,b)
})
}else{init_plpPrice(e,k,l,b)
}}else{if(b==="compare"){e.addClass("plp-item-buybtn eCommerce-buy");
$.each($(".hero-compare__product-item .swatches__item"),function(z,y){var A=o,x=m;
$(y).click(function(){init_plpPrice($(this),A,x,b)
})
});
$.each($(".hero-compare__product-item .swatches__wrapper"),function(y,x){var z=o,i=m;
init_plpPrice($(x).find("div").first().find("button"),z,i,b)
})
}else{if(b==="pdp_relate"){$.each($(".swatches__swatch"),function(z,y){var A=o,x=m;
$(y).click(function(){init_plpPrice($(this),A,x,b)
})
});
$.each($(".relate-product-main .product-li .colorlist"),function(y,x){var z=o,i=m;
init_plpPrice($(x).find("li").first().find("button"),z,i,b)
})
}else{if(b==="series_design"){$.each($(".series-product-list-detail"),function(y,x){var z=o,i=m;
init_plpPrice($(x),z,i,b)
})
}}}}}}else{hideProductEcBuyButton(e,b)
}}else{hideProductEcBuyButton(e,b)
}}}else{handleEcButtons(b);
if(errorCodeMap[v.resultCode]){v.message=ecCom.I18n.get(errorCodeMap[v.resultCode])
}}},function(h,e,f){handleEcButtons(b);
var g=e?e:"Api Fail";
console.error(g+" : queryMinPriceAndInv")
})
}else{handleEcButtons(b)
}}function hideProductEcBuyButton(c,b){if(b=="compare"){var a=PlpI18n.i18n_LearnMore;
c.removeClass("plp-item-buybtn");
c.html(a).attr({"data-buttontype":"explore",title:a})
}else{c.hide()
}}function setComponentButtonText(b){var c,a,d;
switch(b){case"plp_productList":c=$(".product-col");
a=c.find(".product-block__btns button");
break;
case"plp_banner":c=$(".product-listing-hero__container");
a=c.find(".product-listing-hero__buttons a.global-buy-button");
break;
case"pdp_relate":c=$(".relate-product-main .product-li");
a=c.find(".buy-common-btn button");
d=c.find(".buy-common-btn a");
break;
case"series_design":c=$(".series-main .series-product-list");
a=c.find(".btn-container a.series-btn1");
d=c.find(".btn-container a.series-btn2");
break;
default:break
}if(a){a.html(PlpI18n.i18n_Buy).addClass("plp-item-buybtn eCommerce-buy").attr("title",PlpI18n.i18n_Buy)
}if(d){d.html(PlpI18n.i18n_LearnMore).addClass("eCommerce-buy").attr({"data-buttontype":"explore",title:PlpI18n.i18n_LearnMore})
}}function handleEcButtons(c){var b=PlpI18n.i18n_LearnMore;
var d,a,e;
switch(c){case"plp_productList":d=$(".product-col");
a=d.find(".product-block__btns button");
break;
case"plp_banner":d=$(".product-listing-hero__container");
a=d.find(".product-listing-hero__buttons a.global-buy-button");
break;
case"compare":d=$(".hero-compare__product-list .hero-compare__product-item");
e=d.find(".hero-compare__links a");
break;
case"pdp_relate":d=$(".relate-product-main .product-li");
a=d.find(".buy-common-btn button");
e=d.find(".buy-common-btn a");
break;
case"series_design":d=$(".series-main .series-product-list");
a=d.find(".btn-container a.series-btn1");
e=d.find(".btn-container a.series-btn2");
break;
default:break
}if(d){d.find(".plp-item-fromprice").html("")
}if(a){a.hide()
}if(e){e.html(b).addClass("eCommerce-buy").attr({"data-buttontype":"explore",title:b})
}}(function relate_series(){if($(".relate-products-component").length>0){get_relate()
}if($(".series-main").length>0){get_Series()
}})();
function get_relate(){var b=$(".relate-product-main .product-li"),a=[];
$.each(b,function(d,e){var f=$(e).find(".buy-common-btn button").attr("data-ecpid"),c=f&&f!="undefined";
if(f){a.push($(e).find(".buy-common-btn button").attr("data-ecpid"))
}else{a.push(null)
}});
if(window.isECommerceSite=="Self-eCommerce"||window.isECommerceSite=="Fusion-eCommerce"){loadEcData(a,$(".relate-product-main .product-li").first(),"pdp_relate")
}}function get_Series(){var b=$(".series-main .series-product .series-product-list"),a=[];
$.each(b,function(d,e){var f=$(e).find(".btn-container a.series-btn1").attr("data-ecpid"),c=f&&f!="undefined";
if(c){a.push($(e).find(".btn-container a.series-btn1").attr("data-ecpid"))
}else{a.push(null)
}});
if(window.isECommerceSite=="Self-eCommerce"||window.isECommerceSite=="Fusion-eCommerce"){loadEcData(a,$(".series-main .series-product .series-product-list").first(),"series_design")
}}var buttonContainer=$(".product-tabs-wrap .product-tabs__button-container");
var ecomBuyButton=buttonContainer.find("button.product-tabs__button");
if(buttonContainer.length>0&&window.isECommerceSite!="None"){ecomBuyButton.addClass("eCommerce-buy");
buttonContainer.on("click",function(){buyFeature($(this).find("a.product_buy_btn"))
});
var productId=$("#productId").val();
if(productId){if(digitalData.page.category.pageType!="product-detail_buy"){window.getMinPriceAndInv([productId]).then(function(a){if(a.resultCode===0){if(a.data.minPriceAndInvList&&a.data.minPriceAndInvList.length>0){ecomBuyButton.css("display","inherit")
}}})
}}}function getOrderPriceFormatterValue(b){var a=ecCurrency(b);
return enableRRP?'<label style="display:inline-block;">'+RRPText+'</label><label style="text-decoration: line-through;">'+a+"</label>":a
}function ecInstallmentFullText(a){var c="";
var b=a.sort(function(g,f){return f.num-g.num
})[0];
var d=b.num;
if(enableInstallmentCfg){c=window.ecInstallmentInfo(b)
}else{var e=ecCom.I18n.get("ec_payment_in_installments",d);
if(site==="UK"||site==="DE"||site==="ES"){c=ecCom.I18n.get("ec_installment_or")+" "+ecCom.I18n.get("ec_finance_available")
}else{c=ecCom.I18n.get("ec_installment_or")+" "+e
}}return c
}function ecInstallmentInfo(d){var c="";
var h=insatallmentLeftText;
var b=insatallmentRightText;
var a=d.num;
var e=window.ecCurrency(d.amount).replaceAll(" ","");
var g=ecCom.I18n.get("ec_du_montant_de_lachat")==="ec_du_montant_de_lachat"?"No interest charged":ecCom.I18n.get("ec_du_montant_de_lachat");
var f=enableInterestFree&&d.installmentFlag==1?" "+g:"";
if(installmentDispType){switch(installmentDispType){case"numberAndAmount":c=h+" "+a+" × "+e+b+f;
break;
case"amountAndNumber":c=h+" "+e+" × "+a+b+f;
break;
case"onlyAmount":c=h+" "+e+b+f;
break;
case"onlyNumber":c=h+" "+a+b+f;
break;
case"noDisplay":break;
default:console.log("Please configure the installment display type first.")
}}return c
};