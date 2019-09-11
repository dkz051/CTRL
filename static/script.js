(function ($) {
  console.log('© Theme-Vexo | https://github.com/yanm1ng/hexo-theme-vexo')
  var app = $('.app-body')
  var header = $('.header')
  var banner = document.getElementById('article-banner') || false
  var top = $('.scroll-top')

  $(document).ready(function () {
    NProgress.start()
    $('#nprogress .bar').css({
      'background': '#42b983'
    })
    $('#nprogress .spinner').hide()

    var fade = {
      transform: 'translateY(0)',
      opacity: 1
    }
    if (banner) {
      app.css('transition-delay', '0.15s')
      $('#article-banner').children().css(fade)
    } else {
      header.addClass('fixed-header')
    }
    if ((document.documentElement.scrollTop || document.body.scrollTop) > 0) {
      header.addClass('header-border')
    }
    app.css(fade)
  })

  window.onload = function () {
    setTimeout(function () {
      NProgress.done()
    }, 200)
  }

  $('.item-icon-link').on('click', function() {
    $('#search-form').fadeToggle()
  })

  $('.arrow-down').on('click', function () {
    $('html, body').animate({
      scrollTop: banner.offsetHeight - header.height()
    }, 500)
  })

  top.on('click', function () {
    $('html, body').animate({ scrollTop: 0 }, 600)
  })

  document.addEventListener('scroll', function () {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop
    if (scrollTop > 0) {
      if (banner) header.addClass('fixed-header')
      header.addClass('header-border')
    } else if (scrollTop === 0) {
      if (banner) header.removeClass('fixed-header')
      header.removeClass('header-border')
    }
    if (scrollTop > 100) {
      top.addClass('opacity')
    } else {
      top.removeClass('opacity')
    }
  })

  $("#search-form").submit(function() {
    var newUrl = '/search/' + $(".search-box")[0].value + '/'
    window.location.href = newUrl
    return false
  })

  $("#crawl-update").click(function() {
    $.get("//localhost:6800/listjobs.json", { project: "bot" }, function(jobs) {
      if (jobs["running"].length <= 0 && jobs["pending"].length <= 0) {
        $.post("//localhost:6800/schedule.json", { project: "bot", spider: "bot" }, function() {
          alert("成功添加爬虫任务")
        });
      } else {
        alert("当前已经在进行后台爬取了")
      }
    })
  })

  $("#crawl-cancel").click(function() {
    $.get("//localhost:6800/listjobs.json", { project: "bot" }, function(jobs) {
      running_jobs = jobs["running"]
      pending_jobs = jobs["pending"]
      if (running_jobs.length <= 0 && pending_jobs.length <= 0) {
        alert("当前没有运行任何爬虫任务")
      } else {
        if (running_jobs.length > 0) {
          $.post("//localhost:6800/cancel.json", { project: "bot", job: running_jobs[0]["id"]}, function() {
            alert("已取消正在运行的爬虫任务")
          })
        }
        if (pending_jobs.length > 0) {
          $.post("//localhost:6800/cancel.json", { project: "bot", job: pending_jobs[0]["id"]}, function() {
            alert("已取消正在运行的爬虫任务")
          })
        }
      }
    })
  })

  $("#return-back").click(function() {
    window.history.go(-1)
  })
})(jQuery)
