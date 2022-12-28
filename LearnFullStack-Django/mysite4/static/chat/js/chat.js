// $('.conLeft li').on('click', function () {
//     $(this).addClass('bg').siblings().removeClass('bg');
//     var intername = $(this).children('.liRight').children('.intername').text();
//     $('.headName').text(intername);
//     $('.newsList').html('');
// });
$('.sendBtn').on('click', function () {
    var news = $('#dope').val();
    if (news == '') {
        alert('不能为空');
    }
    else {
        $('#dope').val('');
        var str = '';
        str += '<li>' + '<div class="answerHead"><img src="static/chat/img/6.jpg"/></div>' + '<div class="answers">  <img class="jiao" src="static/chat/img/youjiao.jpg">' + news + '</div>' + '</li>';
        $('.newsList').append(str);
        setTimeout(answers(news), 1000);
        $('.conLeft').find('li.bg').children('.liRight').children('.infor').text(news);
        $('.RightCont').scrollTop($('.RightCont')[0].scrollHeight);
    }
});
function createXMLHttpRequest() {
            try {
                return new XMLHttpRequest();//大多数浏览器
            } catch (e) {
                try {
                    return new ActiveXObject("Msxml2.XMLHTTP");
                } catch (e) {
                    return new ActiveXObject("Microsoft.XMLHTTP");
                }
            }
        }
function answers(news) {

            var xmlHttp = createXMLHttpRequest();

            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                    // var div = document.getElementById("div1");
                    // div.innerText = xmlHttp.responseText;
                    // div.textContent = xmlHttp.responseText;
                    var a = xmlHttp.responseText
                    var answer = '';
                    answer += '<li>' + '<div class="nesHead"><img src=static/chat/img/tou.jpg></div>' + '<div class="news">' +
                        '<img class="jiao" src="static/chat/img/youjiao.jpg">' +a+ '</div>' + '</li>';
                    $('.newsList').append(answer);
                    $('.RightCont').scrollTop($('.RightCont')[0].scrollHeight);

                }
                ;
            }
            xmlHttp.open("POST", "/ajax_post", true);

            xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

            xmlHttp.send('new='+news);  //post: xmlHttp.send("b=B");
        }

$('.ExP').on('mouseenter', function () {
    $('.emjon').show();
});
$('.emjon').on('mouseleave', function () {
    $('.emjon').hide();
});
$('.emjon li').on('click', function () {
    var imgSrc = $(this).children('img').attr('src');
    var str = "";
    str += '<li>' + '<div class="nesHead"><img src="img/6.jpg"/></div>' + '<div class="news"><img class="jiao" src="img/20170926103645_03_02.jpg"><img class="Expr" src="' + imgSrc + '"></div>' + '</li>';
    $('.newsList').append(str);
    $('.emjon').hide();
    $('.RightCont').scrollTop($('.RightCont')[0].scrollHeight);
});
