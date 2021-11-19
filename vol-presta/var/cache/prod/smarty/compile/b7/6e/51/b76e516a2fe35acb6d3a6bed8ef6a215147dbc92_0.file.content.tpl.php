<?php
/* Smarty version 3.1.39, created on 2021-11-19 12:24:26
  from '/var/www/html/admin1437/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6197896a5b4012_84446321',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'b76e516a2fe35acb6d3a6bed8ef6a215147dbc92' => 
    array (
      0 => '/var/www/html/admin1437/themes/default/template/content.tpl',
      1 => 1637305681,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6197896a5b4012_84446321 (Smarty_Internal_Template $_smarty_tpl) {
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
