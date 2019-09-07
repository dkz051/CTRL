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
    $('.search-box').fadeToggle()
  })

  /*$('.menu').on('click', function () {
    if (!header.hasClass('fixed-header') || isOpen) {
      header.toggleClass('fixed-header')
      isOpen = !isOpen
    }
    $('.menu-mask').toggleClass('open')
  })*/

  $('.arrow-down').on('click', function () {
    $('html, body').animate({
      scrollTop: banner.offsetHeight - header.height()
    }, 500)
  })

  $('.toc-nav a').on('click', function (e) {
    e.preventDefault()
    var catalogTarget = e.currentTarget
    var scrollTarget = $(catalogTarget.getAttribute('href'))
    var top = scrollTarget.offset().top
    if (top > 0) {
      $('html,body').animate({
        scrollTop: top - 65
      }, 500)
    }
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

  $("#searchform").submit(function() {
    var newUrl = '/search/' + $("#search-box")[0].value + '/';
    $("#searchform").attr('action', newUrl);
    $("#searchform").submit();
  })
})(jQuery)

