<?php
/* Smarty version 3.1.39, created on 2021-11-20 16:24:04
  from '/var/www/html/admin1437/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_61991314381749_50955945',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'b76e516a2fe35acb6d3a6bed8ef6a215147dbc92' => 
    array (
      0 => '/var/www/html/admin1437/themes/default/template/content.tpl',
      1 => 1637346905,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_61991314381749_50955945 (Smarty_Internal_Template $_smarty_tpl) {
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
