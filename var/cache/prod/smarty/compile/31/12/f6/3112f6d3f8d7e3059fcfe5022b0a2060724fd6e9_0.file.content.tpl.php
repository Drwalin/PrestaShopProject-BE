<?php
/* Smarty version 3.1.39, created on 2021-11-06 15:05:10
  from '/var/www/html/prestashop/admin1/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_61868b96afa2b6_57961169',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '3112f6d3f8d7e3059fcfe5022b0a2060724fd6e9' => 
    array (
      0 => '/var/www/html/prestashop/admin1/themes/new-theme/template/content.tpl',
      1 => 1633801229,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_61868b96afa2b6_57961169 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
