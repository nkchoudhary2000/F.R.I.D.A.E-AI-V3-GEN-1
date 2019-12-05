import sublime
import sublime_plugin



class StandardTemplate(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		for sel in sels:
			standard = self.view.substr(sel).split('\n')
			print(standard)
			if "spark_panel" == standard[0]:
				self.view.replace(edit, sel, sparkPanel)
			if "trigger" == standard[0]:
				self.view.replace(edit, sel, trigger)


#########################################################
##        TRIGGERED WALMART 52A DIRECTORY
#########################################################
trigger = """<?xml version="1.0" encoding="UTF-8"?>
<survey 
	alt=[Triggered Survey Name]
	autosave="0"
	builder:cname="walmart.decipherinc.com"
	builder:wizardCompleted="1"
	builderCompatible="1"
	compat="143"
	delphi="1"
	displayOnError="all"
	extraVariables="source,record,ipAddress,decLang,list,userAgent"
	fir="on"
	html:showNumber="0"
	mobile="compat"
	mobileDevices="smartphone,tablet,desktop"
	name="Survey"
	secure="1"
	setup="term,decLang,quota,time"
	ss:disableBackButton="0"
	ss:enableNavigation="1"
	ss:hideProgressBar="0"
	state="testing"
	theme="company/walmart-standard-2">

<res label="continueButton">Continue</res>
<res label="supportLinks"><a href="http://www.survey.walmart.com/Surveys/WM/StoreTrak/rules_new_en.htm?date={}" class="help" target="_blank">Official Sweepstakes Rules</a> - <a href="http://corporate.walmart.com/privacy-security/walmart-privacy-policy" class="help" target="_blank">Privacy Policy</a> - <a href="mailto:surveysupport@walmart.com?subject=Survey Feedback - {}" target="_blank" class="help">Help</a></res>
<samplesources default="0">
	<samplesource list="0">
		<title>Open Survey</title>
		<invalid>You are missing information in the URL. Please verify the URL with the original invite.</invalid>
		<completed>It seems you have already entered this survey.</completed>
		<var name="source" unique="1"/>
		<exit cond="terminated">Thank you for taking our survey.</exit>
		<exit cond="qualified">Thank you for taking our survey. Your efforts are greatly appreciated!</exit>
		<exit cond="overquota">Thank you for taking our survey.</exit>
	</samplesource>
</samplesources>

<suspend/>

<style name="button.continue"><![CDATA[
<input type="submit" name="continue" id="btn_continue" class="button continue" value="${res.continueButton}" onClick="var i = document.createElement('input');i.setAttribute('type', 'hidden');i.setAttribute('value', '1');i.setAttribute('name', '__has_javascript');document.forms.primary.appendChild(i);"/>
]]></style>
<style name="button.goback"><![CDATA[
<input type="button" id="btn_goback" class="button continue" onClick="Survey.postControl('back2')" value="@(back)" />
]]></style>
<style name="survey.logo"><![CDATA[
<div class="logo logo-$(gv.survey.root.styles.ss.logoPosition)">
<svg width="133px" height="33px" viewBox="0 0 133 33" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><polygon id="path-1" points="0.147343387 0.125714286 28.9334443 0.125714286 28.9334443 32.3713657 0.147343387 32.3713657"></polygon></defs><g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="Clean---01" transform="translate(-33.000000, -19.000000)"><g id="Group-6" transform="translate(33.000000, 19.000000)"><path d="M47.8318276,11.647938 L47.8318276,13.5551867 L47.88773,13.5551867 C48.5320127,12.5344101 49.5935334,11.3313184 51.9564241,11.3313184 C53.7952689,11.3313184 55.2059452,12.3291879 55.8061932,13.8416819 L55.8620956,13.8416819 C56.3789584,13.0794728 56.9710864,12.500834 57.631609,12.0932138 C58.4176777,11.6087136 59.2868192,11.3313184 60.3883147,11.3313184 C62.8755023,11.3313184 65.0784934,13.0575071 65.0784934,17.4170672 L65.0784934,25.6836942 L61.2836898,25.6836942 L61.2836898,17.9931956 C61.2836898,15.7834481 60.5382206,14.5053593 58.985446,14.5053593 C57.8467863,14.5053593 57.0198058,15.2722753 56.7078143,16.2152306 C56.6000695,16.5409503 56.5497886,16.9843433 56.5497886,17.3530529 L56.5497886,25.6836942 L52.7577956,25.6836942 L52.7577956,17.6844209 C52.7577956,15.806669 52.0410584,14.5053593 50.5095205,14.5053593 C49.2840403,14.5053593 48.5170222,15.4746734 48.2025322,16.3034072 C48.0685539,16.6586236 48.024519,17.0665577 48.024519,17.4522123 L48.024519,25.6836942 L44.2284662,25.6836942 L44.2284662,11.647938 L47.8318276,11.647938 Z M84.6580688,11.647938 L84.6580688,14.2954301 L84.7636274,14.2954301 C85.4575665,12.2742737 87.1115275,11.3313184 88.5649895,11.3313184 C88.9300726,11.3313184 89.1302594,11.3589324 89.4235127,11.417926 L89.4235127,15.0930982 C89.0737324,15.0419495 88.7508102,14.9929974 88.2992189,14.9929974 C86.6543147,14.9929974 85.508472,15.9550942 85.2199033,17.4609985 C85.1590041,17.7707146 85.1355813,18.1089861 85.1355813,18.4968373 L85.1355813,25.6836942 L81.2402158,25.6836942 L81.2402158,11.647938 L84.6580688,11.647938 Z M94.7114408,7.0003138 L94.7114408,11.417926 L98,11.417926 L98,14.9929974 L94.7114408,14.9929974 L94.7114408,20.266016 C94.7114408,21.9721218 95.1430447,22.7999141 96.4291118,22.7999141 C97.0349812,22.7999141 97.4781403,22.7236618 97.8632109,22.6285818 L97.9119303,25.5930073 C97.3944429,25.7869329 96.2957581,26 95.1792719,26 C93.8663467,26 92.7704726,25.5390345 92.1052655,24.827974 C91.3438688,24.0146163 90.9878425,22.683496 90.9878425,20.7831508 L90.9878425,7.0003138 L94.7114408,7.0003138 Z M37.8081244,25.6836942 L41.5838775,25.6836942 L41.5838775,7 L37.8081244,7 L37.8081244,25.6836942 Z M31.5170763,20.6695569 C31.5170763,20.9287519 31.4949028,21.1961056 31.4236975,21.4295694 C31.1313811,22.4020215 30.1288859,23.2238518 28.8752984,23.2238518 C27.8306421,23.2238518 27.0002263,22.6279542 27.0002263,21.3671241 C27.0002263,19.4394788 29.1126493,18.9060265 31.5170763,18.9188921 L31.5170763,20.6695569 Z M35.2890818,17.3100629 C35.2890818,14.1291186 33.9374309,11.3313184 29.3687384,11.3313184 C27.0220875,11.3313184 25.1595076,11.9934268 24.1442079,12.5830484 L24.8871787,15.1392261 C25.8162825,14.5505458 27.2956657,14.0632215 28.6969729,14.0632215 C31.0164533,14.0572594 31.3959024,15.38179 31.3959024,16.2306066 L31.3959024,16.4314357 C26.3415775,16.4239046 23.1492079,18.1811591 23.1492079,21.763134 C23.1492079,23.9502882 24.7741247,26 27.6001619,26 C29.3400064,26 30.7947176,25.3027465 31.6666699,24.1856348 L31.7519288,24.1856348 C31.7519288,24.1856348 32.3293785,26.6115873 35.5105052,25.6836942 C35.3434227,24.6739005 35.2890818,23.5975821 35.2890818,22.301607 L35.2890818,17.3100629 Z M4.17643891,7.0003138 C4.56588176,8.97816644 5.67580952,14.7187402 5.67580952,14.7187402 C6.1405176,17.0791095 6.56993534,19.5537003 6.89254518,21.5105287 L6.94938447,21.5105287 C7.26387442,19.4325753 7.75887596,17.4638227 8.28791862,15.0250045 L10.1558077,7.0003138 L14.2878995,7.0003138 L16.0339901,15.2324233 C16.4924521,17.52313 16.857223,19.2869742 17.1439179,21.4173314 L17.2004449,21.4173314 C17.5158717,19.2662637 17.9243651,17.4286776 18.3756441,15.0777222 L20.0527156,7.0003138 L24.0183494,7.0003138 L19.1061227,25.6836942 C15.9768385,26.372789 14.7779042,25.107252 14.3466126,23.0983336 C13.9171949,21.0887876 13.0783468,17.2629936 13.0783468,17.2629936 C12.6483045,15.1687229 12.3119533,13.6907463 12.0758516,11.5403062 L12.0171385,11.5403062 C11.6810996,13.669722 11.3303824,15.1618194 10.8078981,17.2551487 L8.74638062,25.6836942 C5.5515126,26.3228955 4.44314637,25.3752333 3.82822016,22.7999141 C3.30136362,20.5936184 0,7.0003138 0,7.0003138 L4.17643891,7.0003138 Z M74.9497924,20.6695569 C74.9497924,20.9287519 74.9269942,21.1961056 74.8561012,21.4295694 C74.5640972,22.4020215 73.5612896,23.2238518 72.3077021,23.2238518 C71.2627336,23.2238518 70.4323177,22.6279542 70.4323177,21.3671241 C70.4323177,19.4394788 72.545053,18.9060265 74.9497924,18.9188921 L74.9497924,20.6695569 Z M78.7224225,17.3100629 C78.7224225,14.1291186 77.3701469,11.3313184 72.8011421,11.3313184 C70.4551159,11.3313184 68.5925359,11.9934268 67.5762993,12.5830484 L68.3205193,15.1392261 C69.2489986,14.5505458 70.7296309,14.0632215 72.1300012,14.0632215 C74.4476078,14.0572594 74.8279939,15.38179 74.8279939,16.2306066 L74.8279939,16.4314357 C69.7742936,16.4239046 66.5812994,18.1811591 66.5812994,21.763134 C66.5812994,23.9502882 68.2077776,26 71.0347518,26 C72.7730348,26 74.2286829,25.3027465 75.0987613,24.1856348 L75.1849572,24.1856348 C75.1849572,24.1856348 75.7620946,26.6115873 78.9432213,25.6836942 C78.7761387,24.6739005 78.7224225,23.5975821 78.7224225,22.301607 L78.7224225,17.3100629 Z" id="Fill-1" fill="#FFFFFF"></path><g id="Group-5" transform="translate(104.000000, 0.000000)"><mask id="mask-2" fill="white"><use xlink:href="#path-1"></use></mask><g id="Clip-4"></g><path d="M9.9695229,18.88348 C10.3474414,19.5375086 10.3181528,20.2701086 9.91881882,20.6001086 L2.96984145,25.4595943 C2.24833195,25.8757086 1.16433557,25.3715943 0.549273122,24.3111943 C-0.0673639819,23.2479657 0.0422323982,22.0599657 0.763426968,21.6416514 L8.45658896,18.0707371 C8.93812018,17.8897086 9.59160434,18.2288229 9.9695229,18.88348 M19.1110577,18.88348 C19.4899211,18.2288229 20.1415157,17.8897086 20.6230469,18.0707371 L28.3171537,21.6416514 C29.0414976,22.0599657 29.1454252,23.2479657 28.5331971,24.3111943 C27.9156152,25.3715943 26.8303591,25.8757086 26.1101093,25.4595943 L19.1611319,20.6001086 C18.7636876,20.2701086 18.7331392,19.5365657 19.1110577,18.88348 M14.5385582,21.5187657 C15.295655,21.5187657 15.917331,21.9091086 16.0017329,22.41668 L16.7496967,30.8524229 C16.7496967,31.6877943 15.7708876,32.3713657 14.539503,32.3713657 C13.3103229,32.3713657 12.3327736,31.6877943 12.3327736,30.8524229 L13.0791627,22.41668 C13.1619899,21.9091086 13.7846107,21.5187657 14.5385582,21.5187657 M19.1611319,11.9022514 L26.1101093,7.03899429 C26.8303591,6.62162286 27.9156152,7.12385143 28.5331971,8.18739429 C29.1454252,9.25030857 29.0414976,10.4373657 28.3171537,10.8541086 L20.6230469,14.4291086 C20.1415157,14.6079371 19.4892912,14.2681943 19.1110577,13.6147943 C18.7331392,12.96108 18.7636876,12.2281657 19.1611319,11.9022514 M8.45658896,14.4291086 L0.763426968,10.8541086 C0.0422323982,10.4373657 -0.0673639819,9.25030857 0.549273122,8.18739429 C1.16433557,7.12385143 2.24833195,6.62162286 2.96984145,7.03899429 L9.91881882,11.9022514 C10.3181528,12.2281657 10.3474414,12.9601371 9.96920796,13.6147943 C9.59160434,14.26788 8.93812018,14.6079371 8.45658896,14.4291086 M13.0791627,10.0809657 L12.3327736,1.64490857 C12.3327736,0.810794286 13.3103229,0.125651429 14.539503,0.125651429 C15.7708876,0.125651429 16.7496967,0.810794286 16.7496967,1.64490857 L16.0017329,10.0809657 C15.917331,10.5891657 15.295655,10.9813943 14.5385582,10.9813943 C13.7846107,10.9813943 13.1619899,10.5891657 13.0791627,10.0809657" id="Fill-3" fill="#FFC220" mask="url(#mask-2)"></path></g></g></g></g></svg>
</div>
<!-- /.logo -->
]]></style>
<style name="respview.client.js"><![CDATA[
<script>
$ (document).ready(function() {

/****** Add Background Banner *****/
\@if device.desktop
	$ ('.survey-container').append("<div class='background-header'/>")
\@endif
/**********************************/

/***** set support links to bottom *****/
var mobileTextboxFocus = false;
var $footer = $ ('.survey-section').last();
$footer.addClass('sticky-footer');

	function checkSupportLink() {
		$footer.css('visibility', 'hidden');
		setTimeout(function() {
			let h = $ ('.survey-body').outerHeight();
			let y = Math.ceil($ ('.survey-section').last().position().top);
			if ( h <= y  ) {
				$footer.addClass('sticky-footer');
			} else {
				$footer.removeClass('sticky-footer');
			}
		},300);
		$footer.css('visibility', 'visible');
	}

checkSupportLink();

\@if device.desktop
	$ (window).resize(function() {
		checkSupportLink();
	});
\@else
	$ (window).resize(function() {
		if ( $ ('.textarea').is(':focus') || $ ('.text-input').is(':focus') ) {
			mobileTextboxFocus = true;
			checkSupportLink();
		} else if ( (!$ ('.textarea').is(':focus') || !$ ('.text-input').is(':focus')) && mobileTextboxFocus === true ) {
			mobileTextboxFocus = false;
			checkSupportLink();
		}
	});
\@endif
/**************************************/

		// Updating the Exit Page
		if ( $ ('.exit-message').length > 0 ) {
				let $logo = $ ('.logo');
				let s = '<svg width="91px" height="102px" viewBox="0 0 25 28" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><polygon id="path-1" points="0.127020162 0.108374384 24.9426244 0.108374384 24.9426244 27.9063498 0.127020162 27.9063498"></polygon></defs><g id="Designs" stroke="#fdc300" stroke-width="1" fill="#fdc300" fill-rule="evenodd"><g id="02---selected-copy" transform="translate(-79.000000, -330.000000)"><g id="Group-5-Copy-6" transform="translate(79.000000, 330.000000)"><mask id="mask-2" fill="#fdc300"><use xlink:href="#path-1"></use></mask><g id="Clip-4"></g><g id="Clip-4"></g><path d="M8.59441629,16.2788621 C8.92020814,16.8426798 8.89495928,17.4742315 8.55070588,17.7587143 L2.56020814,21.9479261 C1.93821719,22.3066453 1.00373756,21.872064 0.473511312,20.9579261 C-0.0580723982,20.0413498 0.0364072398,19.0172118 0.658126697,18.6565961 L7.2901629,15.5782217 C7.70527602,15.4221626 8.26862443,15.7145025 8.59441629,16.2788621 M16.4750498,16.2788621 C16.8016561,15.7145025 17.3633756,15.4221626 17.7784887,15.5782217 L24.4113394,18.6565961 C25.0357738,19.0172118 25.1253665,20.0413498 24.5975837,20.9579261 C24.0651855,21.872064 23.1296199,22.3066453 22.5087149,21.9479261 L16.5182172,17.7587143 C16.1755928,17.4742315 16.1492579,16.841867 16.4750498,16.2788621 M12.5332398,18.5506601 C13.1859095,18.5506601 13.7218371,18.8871626 13.7945973,19.3247241 L14.4393937,26.5969163 C14.4393937,27.317064 13.5955928,27.9063498 12.5340543,27.9063498 C11.4744163,27.9063498 10.6317014,27.317064 10.6317014,26.5969163 L11.2751403,19.3247241 C11.346543,18.8871626 11.8832851,18.5506601 12.5332398,18.5506601 M16.5182172,10.2605616 L22.5087149,6.06809852 C23.1296199,5.70829557 24.0651855,6.14125123 24.5975837,7.05809852 C25.1253665,7.97440394 25.0357738,8.99772906 24.4113394,9.35699015 L17.7784887,12.4388867 C17.3633756,12.5930493 16.8011131,12.3001675 16.4750498,11.7368916 C16.1492579,11.1733448 16.1755928,10.5415222 16.5182172,10.2605616 M7.2901629,12.4388867 L0.658126697,9.35699015 C0.0364072398,8.99772906 -0.0580723982,7.97440394 0.473511312,7.05809852 C1.00373756,6.14125123 1.93821719,5.70829557 2.56020814,6.06809852 L8.55070588,10.2605616 C8.89495928,10.5415222 8.92020814,11.172532 8.5941448,11.7368916 C8.26862443,12.2998966 7.70527602,12.5930493 7.2901629,12.4388867 M11.2751403,8.69048768 L10.6317014,1.41802463 C10.6317014,0.698960591 11.4744163,0.108320197 12.5340543,0.108320197 C13.5955928,0.108320197 14.4393937,0.698960591 14.4393937,1.41802463 L13.7945973,8.69048768 C13.7218371,9.12859113 13.1859095,9.46671921 12.5332398,9.46671921 C11.8832851,9.46671921 11.346543,9.12859113 11.2751403,8.69048768" id="Fill-3" stroke="#fdc300" mask="url(#mask-2)"></path></g></g></g></svg>'

			 \@if device.desktop
			 $ ('body').css({
					 'background-color': '#041e42',
			 });
			 \@endif

			 $ ('.survey-body').css({
					 \@if device.desktop
					 'min-height': '400px',
					 \@endif
					 'background-color': '#041e42',
					 'height': '90vh'
			 });
			 $ ('.logo').removeClass('logo-left');
			 $ ('.logo').removeClass('logo-');
			 $ ('.logo').addClass('logo-center');
			 $logo.css({
					 'text-align': 'center',
					 'padding-top': '150px'
			 });
			 $logo.empty();
			 $ ('.logo').append(s);
		}

});
</script>
]]></style>
<suspend/>

<quota label="Total" overquota="noqual" sheet="Overall"/>

<textarea 
	label="QFB2"
	height="10"
	width="50">
	<title>We love to hear from our customers. Is there anything you'd like to share with us today?</title>
</textarea>
<suspend/>

</survey>"""



#########################################################
##        SPARKPANEL WALMART 52B DIRECTORY
#########################################################

sparkPanel ="""<?xml version="1.0" encoding="UTF-8"?>
<survey 
  alt=[Enter Survey Name]
  autosave="0"
  builder:cname="walmart.decipherinc.com"
  builder:wizardCompleted="1"
  builderCompatible="1"
  compat="143"
  delphi="1"
  displayOnError="all"
  extraVariables="source,record,decLang,list,ipAddress, userAgent"
  fir="on"
  html:showNumber="0"
  mobile="compat"
  mobileDevices="smartphone,tablet,desktop"
  name="Survey"
  secure="1"
  setup="term,decLang,quota,time"
  ss:disableBackButton="1"
  ss:enableNavigation="0"
  ss:hideProgressBar="0"
  ss:logoAlt="Logo"
  ss:logoFile="selfserve/53b/Customer-Spark-Small-size.png"
  ss:logoPosition="left"
  state="testing"
  theme="company/walmart-03">



<style name="survey.respview.footer.support"><![CDATA[
<a href="https://corporate.walmart.com/privacy-security/walmart-privacy-policy" target="_blank">Privacy Policy</a> - <a href="mailto:customersparksurvey@walmart.com?Subject=Survey Feedback - ${gv.survey.path.strip('selfserve/')}" target="_blank">Help</a>
]]></style>
<suspend/>

<condition label="Walmart_Customer_Spark_Panel" cond="(list=='200')">Walmart Customer Spark Panel</condition>
<samplesources>
  <samplesource kinesis:pid="1" kinesis:url="walmart.opinioninsight.com" list="200">
    <title>Walmart Customer Spark Panel</title>
    <invalid>You are missing information in the URL. Please verify the URL with the original invite.</invalid>
    <completed>It seems you have already entered this survey.</completed>
    <var name="panelist_hash" unique="1"/>
    <var name="campaign_hash" required="1"/>
    <exit cond="terminated">Click <a href="https://customersparksurvey.walmart.com/portal/community_1_1_1.php" target="_blank">here</a> to login, check and redeem points! <br /><br />Thank you for taking our survey.</exit>
    <exit cond="overquota">Thank you for your interest. This survey has reached its response limit. Be on the lookout for future Spark opportunities.</exit>
    <exit cond="qualified"><span style="font-size: 23px;">Congratulations! You just earned points. Click <a href="https://customersparksurvey.walmart.com/portal/community_1_1_1.php" target="_blank">here</a> to login, check and redeem points!</span> <br /><br />Thanks so much. Walmart was founded on putting you, the customer, first. Your feedback is invaluable.</exit>
  </samplesource>
</samplesources>

<suspend/>

<datasource label="ds1" cond="condition.Walmart_Customer_Spark_Panel" builder:title="Walmart Customer Spark Panel" datasourceKey="panelist_hash" filename="@kinesis" kinesis:pid="1" kinesis:url="walmart.opinioninsight.com" normalizeKey="none" ourKey="panelist_hash" where="execute,survey,report">
  <radio 
   label="ds1_dp_SegQual2"
   dataRef="SegQual2"
   dataSource="ds1"
   kinesis:dpl="SegQual2"
   optional="1"
   where="execute,survey,report">
    <title>Segmentation</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="5" value="1">Segment 1 - Budget Sensitive Busy Families</row>
    <row label="r2" dataValue="6" value="2">Segment 2 - Pragmatic Convenience Seekers</row>
    <row label="r3" dataValue="7" value="3">Segment 3 - Deal Seekers</row>
    <row label="r4" dataValue="8" value="4">Segment 4/5 - Time Sensitive Busy Families</row>
    <row label="r5" dataValue="9" value="5">Segment 6 - Quality Bargain Enthusiasts</row>
    <row label="r6" dataValue="10" value="6">Segment 7 - Super Premium Shoppers</row>
  </radio>

  <text 
   label="ds1_dp_srccustid"
   dataRef="srccustid"
   dataSource="ds1"
   kinesis:dpl="srccustid"
   where="execute,survey,report">
    <title>src_cust_id</title>
    <comment>Be specific</comment>
  </text>

  <radio 
   label="ds1_dp_gender"
   dataRef="gender"
   dataSource="ds1"
   kinesis:dpl="gender"
   optional="1"
   where="execute,survey,report">
    <title>What is your gender?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="11" value="1">Male</row>
    <row label="r2" dataValue="12" value="2">Female</row>
    <row label="r3" dataValue="13" value="3">Other&amp;nbsp;</row>
  </radio>

  <number 
   label="ds1_dp_age"
   dataRef="age"
   dataSource="ds1"
   kinesis:dpl="age"
   size="10"
   where="execute,survey,report">
    <title>What is your age?</title>
    <comment>Enter a number</comment>
  </number>

  <radio 
   label="ds1_dp_ageRange"
   dataRef="ageRange"
   dataSource="ds1"
   kinesis:dpl="ageRange"
   optional="1"
   where="execute,survey,report">
    <title>Age Range</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="318" value="1">18-24</row>
    <row label="r2" dataValue="319" value="2">25-34</row>
    <row label="r3" dataValue="320" value="3">35-44</row>
    <row label="r4" dataValue="321" value="4">45-54</row>
    <row label="r5" dataValue="322" value="5">55-74</row>
    <row label="r6" dataValue="323" value="6">75+</row>
  </radio>

  <radio 
   label="ds1_dp_race"
   dataRef="race"
   dataSource="ds1"
   kinesis:dpl="race"
   optional="1"
   where="execute,survey,report">
    <title>Which best describes your race?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="14" value="1">Caucasian / White</row>
    <row label="r2" dataValue="15" value="2">African / African-American</row>
    <row label="r3" dataValue="16" value="3">Asian</row>
    <row label="r4" dataValue="17" value="4">Indigenous Peoples (i.e. Native American, Pacific Islander, Aboriginal, Aleutian)</row>
    <row label="r5" dataValue="18" value="5">Other</row>
    <row label="r6" dataValue="19" value="6">Prefer not to answer</row>
  </radio>

  <radio 
   label="ds1_dp_hisp"
   dataRef="hisp"
   dataSource="ds1"
   kinesis:dpl="hisp"
   optional="1"
   where="execute,survey,report">
    <title>Are you of hispanic or latino origin?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="20" value="1">Yes</row>
    <row label="r2" dataValue="21" value="2">No</row>
    <row label="r3" dataValue="22" value="3">Prefer not to answer</row>
  </radio>

  <checkbox 
   label="ds1_dp_industry"
   dataSource="ds1"
   kinesis:dpl="industry"
   optional="1"
   where="execute,survey,report">
    <title>Do you, or does anyone in your immediate family, work for these types of companies?</title>
    <comment>Select all that apply</comment>
    <row label="r1" dataRef="industry_23" value="1">A marketing research department within a company or a marketing research firm</row>
    <row label="r2" dataRef="industry_24" value="1">An advertising agency or advertising department within a company</row>
    <row label="r3" dataRef="industry_25" value="1">A mass retailer (Walmart, Target, Kmart, etc.)</row>
    <row label="r4" dataRef="industry_26" value="1">A warehouse or discount club</row>
    <row label="r5" dataRef="industry_27" value="1">An online retailer</row>
    <row label="r6" dataRef="industry_28" value="1">The corporate offices of a retail company</row>
    <row label="r7" dataRef="industry_29" value="1">None of these</row>
  </checkbox>

  <radio 
   label="ds1_dp_income"
   dataRef="income"
   dataSource="ds1"
   kinesis:dpl="income"
   optional="1"
   where="execute,survey,report">
    <title>Which category best describes your total household income last year before taxes?&amp;nbsp;Please include income from all sources.</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="30" value="1">Less than $25,000</row>
    <row label="r2" dataValue="31" value="2">$25,000 - $34,999</row>
    <row label="r3" dataValue="32" value="3">$35,000 - $49,999</row>
    <row label="r4" dataValue="33" value="4">$50,000 - $74,999</row>
    <row label="r5" dataValue="34" value="5">$75,000 - $99,999</row>
    <row label="r6" dataValue="35" value="6">$100,000 - $124,999</row>
    <row label="r7" dataValue="36" value="7">$125,000 - $149,999</row>
    <row label="r8" dataValue="37" value="8">$150,000 or more</row>
    <row label="r9" dataValue="38" value="9">Prefer not to answer</row>
  </radio>

  <radio 
   label="ds1_dp_income2"
   dataRef="income2"
   dataSource="ds1"
   kinesis:dpl="income2"
   optional="1"
   where="execute,survey,report">
    <title>income_2</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="324" value="1">Less than 50k</row>
    <row label="r2" dataValue="325" value="2">50k-99,999k</row>
    <row label="r3" dataValue="326" value="3">100k +</row>
    <row label="r4" dataValue="327" value="4">Prefer not to answer</row>
  </radio>

  <radio 
   label="ds1_dp_decision"
   dataRef="decision"
   dataSource="ds1"
   kinesis:dpl="decision"
   optional="1"
   where="execute,survey,report">
    <title>Which best describes your responsibility in making decisions about the products to purchase for your household?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="39" value="1">I do all or most&amp;nbsp;of the decision making</row>
    <row label="r2" dataValue="40" value="2">I equally share the decision making with someone else</row>
    <row label="r3" dataValue="41" value="3">Someone else makes all or&amp;nbsp;most of the decisions</row>
  </radio>

  <radio 
   label="ds1_dp_HH"
   dataRef="HH"
   dataSource="ds1"
   kinesis:dpl="HH"
   optional="1"
   where="execute,survey,report">
    <title>Including yourself, how many people live in your household?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="42" value="1">1</row>
    <row label="r2" dataValue="43" value="2">2</row>
    <row label="r3" dataValue="44" value="3">3</row>
    <row label="r4" dataValue="45" value="4">4</row>
    <row label="r5" dataValue="46" value="5">5 or more</row>
  </radio>

  <radio 
   label="ds1_dp_HHchild"
   dataRef="HHchild"
   dataSource="ds1"
   kinesis:dpl="HHchild"
   optional="1"
   where="execute,survey,report">
    <title>Are there any children under the age of 18 currently living in your household?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="47" value="1">Yes</row>
    <row label="r2" dataValue="48" value="2">No</row>
  </radio>

  <radio 
   label="ds1_dp_HHchildnum"
   dataRef="HHchildnum"
   dataSource="ds1"
   kinesis:dpl="HHchildnum"
   optional="1"
   where="execute,survey,report">
    <title>How many children under the age of 18 are currently living in your household?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="49" value="1">1</row>
    <row label="r2" dataValue="50" value="2">2</row>
    <row label="r3" dataValue="51" value="3">3</row>
    <row label="r4" dataValue="52" value="4">4</row>
    <row label="r5" dataValue="53" value="5">5 or more</row>
  </radio>

  <radio 
   label="ds1_dp_maritalstatus"
   dataRef="maritalstatus"
   dataSource="ds1"
   kinesis:dpl="maritalstatus"
   optional="1"
   where="execute,survey,report">
    <title>What is your current marital status?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="54" value="1">Single</row>
    <row label="r2" dataValue="55" value="2">In a Domestic Partnership/Living together</row>
    <row label="r3" dataValue="56" value="3">Married</row>
    <row label="r4" dataValue="57" value="4">Divorced/Separated</row>
    <row label="r5" dataValue="58" value="5">Widowed</row>
    <row label="r6" dataValue="59" value="6">Prefer not to answer</row>
  </radio>

  <radio 
   label="ds1_dp_educ"
   dataRef="educ"
   dataSource="ds1"
   kinesis:dpl="educ"
   optional="1"
   where="execute,survey,report">
    <title>What is the highest level of education you have completed?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="60" value="1">Some high school or less</row>
    <row label="r2" dataValue="61" value="2">Graduated high school</row>
    <row label="r3" dataValue="62" value="3">Some college or technical school</row>
    <row label="r4" dataValue="63" value="4">Graduated college or technical school</row>
    <row label="r5" dataValue="64" value="5">Post graduate degree</row>
    <row label="r6" dataValue="65" value="6">Prefer not to answer</row>
  </radio>

  <radio 
   label="ds1_dp_employ"
   dataRef="employ"
   dataSource="ds1"
   kinesis:dpl="employ"
   optional="1"
   where="execute,survey,report">
    <title>Which best describes your current employment status?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="66" value="1">Employed full time</row>
    <row label="r2" dataValue="67" value="2">Employed part time</row>
    <row label="r3" dataValue="68" value="3">Full time homemaker</row>
    <row label="r4" dataValue="69" value="4">Full time student</row>
    <row label="r5" dataValue="70" value="5">Part time student</row>
    <row label="r6" dataValue="71" value="6">Retired</row>
    <row label="r7" dataValue="72" value="7">Not currently working</row>
    <row label="r8" dataValue="73" value="8">Prefer not to answer</row>
  </radio>

  <radio 
   label="ds1_dp_homeown"
   dataRef="homeown"
   dataSource="ds1"
   kinesis:dpl="homeown"
   optional="1"
   where="execute,survey,report">
    <title>Do you rent or own your home?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="74" value="1">Own</row>
    <row label="r2" dataValue="75" value="2">Rent</row>
    <row label="r3" dataValue="76" value="3">Other</row>
    <row label="r4" dataValue="77" value="4">Prefer not to answer</row>
  </radio>

  <checkbox 
   label="ds1_dp_shopP6M"
   dataSource="ds1"
   kinesis:dpl="shopP6M"
   optional="1"
   where="execute,survey,report">
    <title>Which of these retailers have you shopped - instore or online - in the past 6 months?</title>
    <comment>Select all that apply</comment>
    <row label="r1" dataRef="shopP6M_78" value="1">Walmart</row>
    <row label="r2" dataRef="shopP6M_79" value="1">Target</row>
    <row label="r3" dataRef="shopP6M_80" value="1">Dollar Stores (Dollar Tree, Family Dollar, Dollar General, etc.)</row>
    <row label="r4" dataRef="shopP6M_81" value="1">Sam's Club</row>
    <row label="r5" dataRef="shopP6M_82" value="1">Costco</row>
    <row label="r6" dataRef="shopP6M_83" value="1">Home Depot</row>
    <row label="r7" dataRef="shopP6M_84" value="1">Kroger</row>
    <row label="r8" dataRef="shopP6M_85" value="1">Amazon.com</row>
    <row label="r9" dataRef="shopP6M_86" value="1">Jet.com</row>
    <row label="r10" dataRef="shopP6M_87" value="1">ebay.com</row>
    <row label="r11" dataRef="shopP6M_88" value="1">None of these</row>
  </checkbox>

  <radio 
   label="ds1_dp_prime"
   dataRef="prime"
   dataSource="ds1"
   kinesis:dpl="prime"
   optional="1"
   where="execute,survey,report">
    <title>Do you currently have an Amazon Prime membership?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="89" value="1">Yes</row>
    <row label="r2" dataValue="90" value="2">No</row>
  </radio>

  <text 
   label="ds1_dp_zipcode"
   dataRef="zipcode"
   dataSource="ds1"
   kinesis:dpl="zipcode"
   where="execute,survey,report">
    <title>What is your zip code?</title>
    <comment>Be specific</comment>
  </text>

  <radio 
   label="ds1_dp_state"
   dataRef="state"
   dataSource="ds1"
   kinesis:dpl="state"
   optional="1"
   where="execute,survey,report">
    <title>State</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="93">1 Alabama</row>
    <row label="r2" dataValue="94">2 Alaska</row>
    <row label="r3" dataValue="95">3 Arizona</row>
    <row label="r4" dataValue="96">4 Arkansas</row>
    <row label="r5" dataValue="97">5 California</row>
    <row label="r6" dataValue="98">6 Colorado</row>
    <row label="r7" dataValue="99">7 Connecticut</row>
    <row label="r8" dataValue="100">8 Delaware</row>
    <row label="r9" dataValue="101">9 District of Columbia</row>
    <row label="r10" dataValue="102">10 Florida</row>
    <row label="r11" dataValue="103">11 Georgia</row>
    <row label="r12" dataValue="104">12 Hawaii</row>
    <row label="r13" dataValue="105">13 Idaho</row>
    <row label="r14" dataValue="106">14 Illinois</row>
    <row label="r15" dataValue="107">15 Indiana</row>
    <row label="r16" dataValue="108">16 Iowa</row>
    <row label="r17" dataValue="109">17 Kansas</row>
    <row label="r18" dataValue="110">18 Kentucky</row>
    <row label="r19" dataValue="111">19 Louisiana</row>
    <row label="r20" dataValue="112">20 Maine</row>
    <row label="r21" dataValue="113">21 Maryland</row>
    <row label="r22" dataValue="114">22 Massachusetts</row>
    <row label="r23" dataValue="115">23 Michigan</row>
    <row label="r24" dataValue="116">24 Minnesota</row>
    <row label="r25" dataValue="117">25 Mississippi</row>
    <row label="r26" dataValue="118">26 Missouri</row>
    <row label="r27" dataValue="119">27 Montana</row>
    <row label="r28" dataValue="120">28 Nebraska</row>
    <row label="r29" dataValue="121">29 Nevada</row>
    <row label="r30" dataValue="122">30 New Hampshire</row>
    <row label="r31" dataValue="123">31 New Jersey</row>
    <row label="r32" dataValue="124">32 New Mexico</row>
    <row label="r33" dataValue="125">33 New York</row>
    <row label="r34" dataValue="126">34 North Carolina</row>
    <row label="r35" dataValue="127">35 North Dakota</row>
    <row label="r36" dataValue="128">36 Ohio</row>
    <row label="r37" dataValue="129">37 Oklahoma</row>
    <row label="r38" dataValue="130">38 Oregon</row>
    <row label="r39" dataValue="131">39 Pennsylvania</row>
    <row label="r40" dataValue="132">40 Rhode Island</row>
    <row label="r41" dataValue="133">41 South Carolina</row>
    <row label="r42" dataValue="134">42 South Dakota</row>
    <row label="r43" dataValue="135">43 Tennessee</row>
    <row label="r44" dataValue="136">44 Texas</row>
    <row label="r45" dataValue="137">45 Utah</row>
    <row label="r46" dataValue="138">46 Vermont</row>
    <row label="r47" dataValue="139">47 Virginia</row>
    <row label="r48" dataValue="140">48 Washington</row>
    <row label="r49" dataValue="141">49 West Virginia</row>
    <row label="r50" dataValue="142">50 Wisconsin</row>
    <row label="r51" dataValue="143">51 Wyoming</row>
  </radio>

  <radio 
   label="ds1_dp_region"
   dataRef="region"
   dataSource="ds1"
   kinesis:dpl="region"
   optional="1"
   where="execute,survey,report">
    <title>Region</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="144">1 Northeast</row>
    <row label="r2" dataValue="145">2 Midwest</row>
    <row label="r3" dataValue="146">3 South</row>
    <row label="r4" dataValue="147">4 West</row>
  </radio>

  <radio 
   label="ds1_dp_hUrbanicity"
   dataRef="hUrbanicity"
   dataSource="ds1"
   kinesis:dpl="hUrbanicity"
   optional="1"
   where="execute,survey,report">
    <title>Urbanicity Classification</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="150" value="1">Very Rural</row>
    <row label="r2" dataValue="151" value="2">Rural</row>
    <row label="r3" dataValue="152" value="3">Suburban</row>
    <row label="r4" dataValue="153" value="4">Urban</row>
    <row label="r5" dataValue="154" value="5">Very Urban</row>
    <row label="r6" dataValue="155" value="6">Unknown</row>
  </radio>

  <radio 
   label="ds1_dp_WMTNPS"
   dataRef="WMTNPS"
   dataSource="ds1"
   kinesis:dpl="WMTNPS"
   optional="1"
   where="execute,survey,report">
    <title>NPS Score for Walmart</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="227">Promoter</row>
    <row label="r2" dataValue="228">Passive</row>
    <row label="r3" dataValue="229">Detractor</row>
  </radio>

  <radio 
   label="ds1_dp_Expecting"
   dataRef="Expecting"
   dataSource="ds1"
   kinesis:dpl="Expecting"
   optional="1"
   where="execute,survey,report">
    <title>Are you currently expecting a baby, or planning on getting pregnant in the next 12 months?</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="243" value="1">Yes, currently expecting</row>
    <row label="r2" dataValue="244" value="2">Yes, planning on getting pregnant</row>
    <row label="r3" dataValue="245" value="3">No</row>
    <row label="r4" dataValue="246" value="9">Prefer not to answer</row>
  </radio>

  <checkbox 
   label="ds1_dp_OnlineGrocery"
   dataSource="ds1"
   kinesis:dpl="OnlineGrocery"
   optional="1"
   where="execute,survey,report">
    <title>Which of the following online grocery delivery services do you use? Select all that apply</title>
    <comment>Select all that apply</comment>
    <row label="r1" dataRef="OnlineGrocery_254" value="1">Walmart</row>
    <row label="r2" dataRef="OnlineGrocery_255" value="2">Amazon Prime Pantry</row>
    <row label="r3" dataRef="OnlineGrocery_256" value="3">AmazonFresh</row>
    <row label="r4" dataRef="OnlineGrocery_257" value="4">Blue Apron</row>
    <row label="r5" dataRef="OnlineGrocery_258" value="5">CobornsDelivers</row>
    <row label="r6" dataRef="OnlineGrocery_259" value="6">Google Express</row>
    <row label="r7" dataRef="OnlineGrocery_260" value="7">Cotsco</row>
    <row label="r8" dataRef="OnlineGrocery_261" value="8">Home Chef</row>
    <row label="r9" dataRef="OnlineGrocery_262" value="9">Instacart</row>
    <row label="r10" dataRef="OnlineGrocery_263" value="10">My Cloud Grocer</row>
    <row label="r11" dataRef="OnlineGrocery_264" value="11">Peapod</row>
    <row label="r12" dataRef="OnlineGrocery_265" value="12">Safeway</row>
    <row label="r13" dataRef="OnlineGrocery_266" value="13">Shipt</row>
    <row label="r14" dataRef="OnlineGrocery_267" value="14">Target</row>
    <row label="r15" dataRef="OnlineGrocery_268" value="15">Walmart</row>
    <row label="r16" dataRef="OnlineGrocery_269" value="16">Whole Foods</row>
    <row label="r17" dataRef="OnlineGrocery_270" value="17">Winder Farms</row>
    <row label="r18" dataRef="OnlineGrocery_271" value="18">Miejer</row>
    <row label="r19" dataRef="OnlineGrocery_272" value="19">Other</row>
    <row label="r20" dataRef="OnlineGrocery_273" value="99">None of the above – I don’t use any grocery delivery services</row>
  </checkbox>

  <checkbox 
   label="ds1_dp_Pets"
   dataSource="ds1"
   kinesis:dpl="Pets"
   optional="1"
   where="execute,survey,report">
    <title>Which of the following animals, if any, do you own? Select all that apply. </title>
    <comment>Select all that apply</comment>
    <row label="r1" dataRef="Pets_274" value="1">Dog</row>
    <row label="r2" dataRef="Pets_275" value="2">Cat</row>
    <row label="r3" dataRef="Pets_276" value="3">Reptile</row>
    <row label="r4" dataRef="Pets_277" value="4">Rodent</row>
    <row label="r5" dataRef="Pets_278" value="5">Fish</row>
    <row label="r6" dataRef="Pets_279" value="6">Other</row>
    <row label="r7" dataRef="Pets_280" value="7">None of the above</row>
  </checkbox>

  <radio 
   label="ds1_dp_ogfy19"
   dataRef="ogfy19"
   dataSource="ds1"
   kinesis:dpl="ogfy19"
   optional="1"
   where="execute,survey,report">
    <title>og_fy19</title>
    <comment>Select one</comment>
    <row label="r1" dataValue="283" value="1">Yes</row>
    <row label="r2" dataValue="284" value="0">No</row>
  </radio>

  <number 
   label="ds1_dp_ogfy19freq"
   dataRef="ogfy19freq"
   dataSource="ds1"
   kinesis:dpl="ogfy19freq"
   size="10"
   where="execute,survey,report">
    <title>og_fy19_freq</title>
    <comment>Enter a number</comment>
  </number>
</datasource>

<suspend/>
<quota label="Total" overquota="noqual" sheet="Overall"/>

<suspend/>


<textarea 
  label="QFB1"
  height="10"
  width="50">
  <title>Do you have any helpful feedback about this survey experience? If so, please explain. If not, enter NA.</title>
</textarea>

<suspend/>

<textarea 
  label="QFB2"
  height="10"
  width="50">
  <title>We love to hear from our customers. Is there anything you'd like to share with us today?</title>
</textarea>
<suspend/>
</survey>"""