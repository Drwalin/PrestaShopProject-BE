<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerOhlrwdn\appProdProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerOhlrwdn/appProdProjectContainer.php') {
    touch(__DIR__.'/ContainerOhlrwdn.legacy');

    return;
}

if (!\class_exists(appProdProjectContainer::class, false)) {
    \class_alias(\ContainerOhlrwdn\appProdProjectContainer::class, appProdProjectContainer::class, false);
}

return new \ContainerOhlrwdn\appProdProjectContainer([
    'container.build_hash' => 'Ohlrwdn',
    'container.build_id' => 'f7de02cc',
    'container.build_time' => 1636207504,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerOhlrwdn');
