<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit123efb0379b22b01ad451b0039c6dd49
{
    public static $classMap = array (
        'CustomText' => __DIR__ . '/../..' . '/classes/CustomText.php',
        'MigrateData' => __DIR__ . '/../..' . '/classes/MigrateData.php',
        'Ps_Customtext' => __DIR__ . '/../..' . '/ps_customtext.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->classMap = ComposerStaticInit123efb0379b22b01ad451b0039c6dd49::$classMap;

        }, null, ClassLoader::class);
    }
}