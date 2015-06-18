// Borrowed from https://github.com/simianhacker/code-by-voice/blob/master/Gulpfile.js
// Copies macros from the git repo into \Natlink\Natlink\MacroSystem
// IMPORTANT: this gulp task overwrites existing files!

var gulp = require('gulp');
var path = require('path');
var source = path.join('.', 'macros', '**', '*');
var destination = '\\NatLink\\NatLink\\MacroSystem';

gulp.task('copy-macros', function () {
    console.log("Copying macros");
    gulp.src(source).pipe(gulp.dest(destination));
});

gulp.task('default', function () {
    gulp.run('copy-macros');
    gulp.watch(source, function (event) {
        gulp.run('copy-macros');
    });
});