<?php
/* Smarty version 3.1.39, created on 2021-11-20 15:42:02
  from 'module:psimagesliderviewstemplat' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6199093a02abe8_22911735',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '6c2108a17c7103b6e203f4f0621d4645b56b0114' => 
    array (
      0 => 'module:psimagesliderviewstemplat',
      1 => 1637346906,
      2 => 'module',
    ),
  ),
  'cache_lifetime' => 31536000,
),true)) {
function content_6199093a02abe8_22911735 (Smarty_Internal_Template $_smarty_tpl) {
?>
  <div id="carousel" data-ride="carousel" class="carousel slide" data-interval="5000" data-wrap="true" data-pause="hover" data-touch="true">
    <ol class="carousel-indicators">
            <li data-target="#carousel" data-slide-to="0" class="active"></li>
            <li data-target="#carousel" data-slide-to="1"></li>
            <li data-target="#carousel" data-slide-to="2"></li>
          </ol>
    <ul class="carousel-inner" role="listbox" aria-label="Carousel container">
              <li class="carousel-item active" role="option" aria-hidden="false">
          <a href="http://localhost/index.php?id_category=8&amp;controller=category">
            <figure>
              <img src="http://localhost/modules/ps_imageslider/images/2cf4094bef1a5c1ecfe78c3c449bc1e5cfdef9e8_banner2.png" alt="sample-2" loading="lazy" width="1110" height="340">
                              <figcaption class="caption">
                  <h2 class="display-1 text-uppercase">SZKOŁA ŚREDNIA</h2>
                  <div class="caption-description"><h3>Kursy dla młodszego brata</h3>
<p>wy debile chodzicie do swietlicy a nie do szkoly</p></div>
                </figcaption>
                          </figure>
          </a>
        </li>
              <li class="carousel-item " role="option" aria-hidden="true">
          <a href="http://localhost/index.php?id_category=3&amp;controller=category">
            <figure>
              <img src="http://localhost/modules/ps_imageslider/images/f629d60b5b75c4ca60919d6a00c61816fe0b3699_banner0.png" alt="sample-1" loading="lazy" width="1110" height="340">
                              <figcaption class="caption">
                  <h2 class="display-1 text-uppercase">KURSY NA STUDIA</h2>
                  <div class="caption-description"><h3>student debil</h3>
<p></p>
<p>piwo piwo alkohol</p></div>
                </figcaption>
                          </figure>
          </a>
        </li>
              <li class="carousel-item " role="option" aria-hidden="true">
          <a href="http://localhost/index.php?id_category=9&amp;controller=category">
            <figure>
              <img src="http://localhost/modules/ps_imageslider/images/72062734af102bf60cac04c98a5c40b2b835f366_banner1.png" alt="sample-3" loading="lazy" width="1110" height="340">
                              <figcaption class="caption">
                  <h2 class="display-1 text-uppercase">Matura podstawowa</h2>
                  <div class="caption-description"><h3>Kursy najwyższej jakości</h3>
<p>serio jakim debilem trza byc zeby nie zdac podstawy co sie z wami dzieje xDDDD</p></div>
                </figcaption>
                          </figure>
          </a>
        </li>
          </ul>
    <div class="direction" aria-label="Przyciski karuzeli">
      <a class="left carousel-control" href="#carousel" role="button" data-slide="prev" aria-label="Poprzedni">
        <span class="icon-prev hidden-xs" aria-hidden="true">
          <i class="material-icons">&#xE5CB;</i>
        </span>
      </a>
      <a class="right carousel-control" href="#carousel" role="button" data-slide="next" aria-label="Następny">
        <span class="icon-next" aria-hidden="true">
          <i class="material-icons">&#xE5CC;</i>
        </span>
      </a>
    </div>
  </div>
<?php }
}
