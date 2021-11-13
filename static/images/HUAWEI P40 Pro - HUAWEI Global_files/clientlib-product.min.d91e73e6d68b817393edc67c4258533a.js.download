var getPdpCookieTipHeight=function(){var a=$(".group_tips").height();
return a
};
function go_buy(){var a=getPdpCookieTipHeight(),c=$(".column13").position().top,b=70;
if(parseInt(window.innerWidth)<768){b=80
}$("html, body").animate({scrollTop:parseInt(c+a-b)+"px"},1000)
}$(document).ready(function(){$(window).scroll(function(){if($(window).scrollTop()>0){var b=$(".region_selector_module.slide_wrap").is(":visible");
var d=$(".search_module.wrap_search.slide_wrap").is(":visible");
var a=$("#normal_nav .icon_menu").is(":visible");
var c=$("#normal_nav .navcon .menu").is(":visible");
if(b||d||(a&&c)||$("[wrap=wrap_phones]").attr("class")=="menu_wrap current"||$("[wrap=wrap_others]").attr("class")=="menu_wrap current"){$("#pdp_nav").css("display","none")
}else{$("#pdp_nav").css("display","block");
setTimeout(function(){if($("#normal_nav").css("display")=="block"){$("#pdp_nav").css("top",getPdpCookieTipHeight())
}else{$("#pdp_nav").css("top",0)
}},50)
}}else{$("#pdp_nav").css("display","none")
}})
});
$(document).ready(function(){var a=document.location.pathname;
if(a.indexOf("/support/")!=-1){$("#pdpComponentButtom").css("display","none");
$("#pdpComponentProductSupport").addClass("current")
}else{if(a.indexOf("/specs")!=-1){$("#pdpComponentSpecification").addClass("current")
}else{if(a.indexOf("/information")!=-1){$("#pdpComponentButtom").css("display","none");
$("#pdpComponentInformationation").addClass("current")
}}}});
var v4_PDPAppStatistic={init:function(){this.sendAppStatisticData()
},callAppStatisticsData:function(c){var e=window.performance.timing.domContentLoadedEventEnd-window.performance.timing.navigationStart;
var d=getMktDmpaSubModuleName();
var a={product_name:c};
var b=JSON.stringify(a);
window.clientJsBridge.call({path:"jsp://com.huawei.phoneservice/track/sendTrack",type:"trackPageView",json:{title:document.title,location:location.href,uri:location.pathname,referrerUrl:"",pageLoadDelay:e,pageHierarchy:0,trackSource:"",trackMedium:"",trackCampaign:"",trackContent:"",trackTerm:"",subModuleName:d,additionalProperty:b}})
},sendAppStatisticData:function(){var a=window.integrationJsInterface||window.integrationJsInterfaceWebview;
var d=window.digitalData;
var c=d.page.category.pageType=="product-detail";
var b=d.product&&d.product.productInfo?d.product.productInfo.marketingName:"";
if(enableAppDmpa&&a&&c&&b.length>0){var e="/etc/designs/huawei-cbg-site/statics/js-bridge.js";
$.getScript(e,function(){v4_PDPAppStatistic.callAppStatisticsData(b)
})
}}};
$(function(){v4_PDPAppStatistic.init()
});
function converString2(a){if(a==null){return""
}else{a=a.toString();
a=a.replace(/<>/g,"");
a=a.replace(/\+/g," ");
a=a.replace(/@\(R\)@/g,"®");
a=a.replace(/@\(-7\)@/g,"&");
a=a.replace(/@\(-8\)@/g,"+");
a=a.replace(/@\(-9\)@/g,"'");
a=a.replace(/@\(TM\)@/g,"™");
a=a.replace(/@\(C\)@/g,"©");
a=a.replace(/&amp;quot;/g,'"');
return a
}}var iscompare=1;
var cpbi2="31001";
var comparedata="";
function defaultCompares(){var c=";";
var d="";
for(var b=1;
b<=4;
b++){var a=getURLParam("pro"+b);
if(a){autoSelect(a,b-1);
if(a){d=d.concat(a).concat(c)
}}}if(d&&d.endsWith(c)){d=d.substring(0,d.length-1)
}if(d){analyticsSubmit("Site Search","Filter by",d+" - <page title>",EVENT_COMPARISON_FILTER,{products:d})
}}function autoSelect(f,c){var a=$(".compare_content .conv3_global_selector .select").eq(c);
var e=a.find("li");
var b=e.length;
for(var d=0;
d<b;
d++){if(f==e.eq(d).attr("n")){selectProductCompare(e.eq(d));
break
}}}function selectProductCompare(d){var c=d.attr("p");
d.parents(".select").addClass("disable");
var a=d.attr("data-product-path");
var b=$(".compare_wrap").data("current-page");
getProInfo(a,c,b)
}function getProInfo(a,c,d){var b=deleteHttp(a.replace("/jcr:content/product",""));
$.ajax({type:"GET",async:false,url:b+"/_jcr_content.compareinfo.json"+d,success:function(e){setCompareInfo(e,c)
}})
}function setCompareInfo(e,c){var f=e.productInfo;
var a=e.productColors;
var d=e.featurePage;
var b=$(".compare_wrap .pro_content").eq(c);
b.addClass("active");
b.find(".column_phone_name").text(f.marketingName).show();
b.find(".column_pic_bg").attr("href",d).append("<img src='"+f.assetPath+"' title='"+f.marketingName+"'>");
b.find(".column_remove_btn").show();
$(".compare_part_base").each(function(){var h=$(this).data("property-key");
var g=converString2(f[h]);
if(h=="color"){g=convertColor(a)
}else{if(h=="size"){g=getSizeDesc(f)
}}$(".compare_property_"+h+" .compare_uList li").eq(c).removeClass("none").append("<i class='compare_txt'>"+g+"</i>")
})
}function newLine(b){var a=/;/g;
return b.replace(a,"; ")
}function newLine2(b){var a=/\//g;
return b.replace(a,", ")
}function convertColor(b){if(!b){return""
}var a=[];
for(var c in b){a.push(b[c])
}return a.join(",")
}function getSizeDesc(g){var e={size_width:$("#compare-product-model").data("width-title"),size_height:$("#compare-product-model").data("height-title"),size_depth:$("#compare-product-model").data("depth-title"),size_weight:$("#compare-product-model").data("weight-title")};
if(g==null||typeof(g)!="object"){return""
}var d=["size_width","size_height","size_depth","size_weight"];
var c=[];
for(var b=0;
b<d.length;
b++){var a=d[b];
if(g[a]){var f=e[a]+":"+g[a];
c.push(f)
}}return c.join(",")
}$(document).on("click",".column_remove_btn",function(b){b=b||window.event;
b.stopPropagation();
var a=$(this).parents(".pro_content");
var f=$(this).attr("p");
var g=$(".compare_wrap .compare_Model .compare_content .compare_list .conv3_global_selector .select").eq(f);
a.find(".column_pic_bg,.column_phone_name").empty();
a.find(".column_phone_name,.column_remove_btn").hide();
a.removeClass("active");
var e=g.find("span").data("text");
g.removeClass("disable").find("span").text(e);
g.find("li").removeClass("current");
$(".compare_wrap .compare_part_base").each(function(h){$(this).find(".compare_uList li").eq(f).empty().addClass("none")
});
var d="";
var c=";";
$(".compare_uList").find("li").each(function(){var h=$(this).find(".column_phone_name").text();
if(h){d=d.concat(h).concat(c)
}});
if(d&&d.endsWith(c)){d=d.substring(0,d.length-1)
}analyticsSubmit("Site Search","Filter by",d+" - <page title>",EVENT_COMPARISON_FILTER,{products:d})
}).on("click",".compare_wrap .compare_center",function(b){if($(".compare_content .column_colse:visible").length>0){var c=$(this),a=c.find(".column_colse");
if(a.hasClass("active")){a.removeClass("active");
c.parent(".compare_title").siblings(".compare_list").stop().slideUp(250)
}else{c.parent(".compare_title").siblings(".compare_list").stop().slideDown(250);
a.addClass("active")
}}}).on("click",".pro_back",function(c){var b=$(this).attr("categoryId")=="31"?$(".menu_module_allphone"):$(".menu_module_tablets");
var a=$(this).attr("categoryId");
if(a=="31"){menuPageHistory.pages.push(".see_all_phone.common_menu.wrap_phones")
}else{if($(".wrap_tablets").length>0&&a=="36"){menuPageHistory.pages.push(".explore.common_menu.wrap_tablets")
}else{menuPageHistory.pages.push(".explore.common_menu.wrap_others")
}}menuPageHistory.PushPage(b.find(".common_menu"),function(){b.find(".see_phone_uList").empty();
setProducts(0,prosize-1,b,a)
})
});
var compare_wrap=$(".compare_wrap"),columnColse=compare_wrap.find(".column_colse");
columnColse.each(function(a){if(viewType()=="mobile"){if(columnColse.eq(a).hasClass("active")){$(this).parent(".compare_center").parent(".compare_title").siblings(".compare_list").css("display","block")
}else{$(this).parent(".compare_center").parent(".compare_title").siblings(".compare_list").css("display","none")
}}});
$(window).resize(function(){columnColse.each(function(a){if(viewType()=="mobile"){if(columnColse.eq(a).hasClass("active")){$(this).parent(".compare_center").parent(".compare_title").siblings(".compare_list").css("display","block")
}else{$(this).parent(".compare_center").parent(".compare_title").siblings(".compare_list").css("display","none")
}}else{if(!columnColse.eq(a).hasClass("active")){$(this).parent(".compare_center").parent(".compare_title").siblings(".compare_list").css("display","block")
}}})
});
$(".compare_list .select ol li").click(function(){var b=this;
var d="";
var c=";";
var a=$(b).closest(".compare_list").find(".select").index($(b).closest(".select"));
$(b).closest(".compare_list").find(".column_phone_name").each(function(f,g){var e=(f==a)?$(b).text():$(g).text();
if(e){d=d.concat(e).concat(c)
}});
if(d.endsWith(c)){d=d.substring(0,d.length-1)
}analyticsSubmit("Site Search","Filter by",d+" - <page title>",EVENT_COMPARISON_FILTER,{products:d})
});
$(document).ready(function(){$(".compare_content .conv3_global_selector").addSelector()
});
$(document).ready(function(){if(window.location.hash.indexOf("#")===0){var a=window.location.hash.substring(1);
if($("#"+a).length>0){setTimeout(function(){$("html,body").animate({scrollTop:$("#"+a).offset().top-100},500)
},200)
}}});