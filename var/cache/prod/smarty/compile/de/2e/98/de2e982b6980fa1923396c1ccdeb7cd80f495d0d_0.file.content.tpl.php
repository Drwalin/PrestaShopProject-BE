<?php
/* Smarty version 3.1.39, created on 2021-11-08 15:32:47
  from '/var/www/html/prestashop/admin1/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6189350fdb4857_68251807',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'de2e982b6980fa1923396c1ccdeb7cd80f495d0d' => 
    array (
      0 => '/var/www/html/prestashop/admin1/themes/default/template/content.tpl',
      1 => 1633801229,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6189350fdb4857_68251807 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
