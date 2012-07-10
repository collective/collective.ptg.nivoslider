from zope.i18nmessageid import MessageFactory
from collective.plonetruegallery.utils import createSettingsFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.plonetruegallery.browser.views.display import \
    BatchingDisplayType
from collective.plonetruegallery.browser.views.display import jsbool
from collective.plonetruegallery.interfaces import IBaseSettings
from zope import schema

_ = MessageFactory('collective.ptg.nivoslider')

class INivosliderDisplaySettings(IBaseSettings):
    nivoslider_width = schema.Int(
        title=_(u"label_nivoslider_width",
            default=u"Width of the gallery in pixels"),
        default=600)
    nivoslider_height = schema.Int(
        title=_(u"label_nivoslider_height",
            default=u"Height of the gallery in pixels"),
        default=350)
    nivoslider_theme = schema.Choice(
        title=_(u"nivoslider_theme", default=u"Nivoslider Theme"),
        default=u"default",
        vocabulary=SimpleVocabulary([
            SimpleTerm("default", "default",
                _(u"label_nivoslider_theme1", default=u"Default Theme")),
            SimpleTerm("orman", "orman",
                _(u"label_nivoslider_theme2", default=u"Orman Theme")),
            SimpleTerm("pascal", "pascal",
                _(u"label_nivoslider_theme3", default=u"Pascal Theme")),
            SimpleTerm("oldframe", "oldframe",
                _(u"label_nivoslider_theme4", default=u"Old Frame Theme")),
            SimpleTerm("overlay", "overlay",
                _(u"label_nivoslider_theme5", default=u"Overlay Theme")),
            SimpleTerm("bendit", "bendit",
                _(u"label_nivoslider_theme6", default=u"Bendit Theme")),
            SimpleTerm("tv", "tv",
                _(u"label_nivoslider_theme7", default=u"TV Theme")),
            SimpleTerm("thumbnail", "thumbnail",
                _(u"label_nivoslider_theme8", default=u"Thumbnail Theme")
            )
        ]))
    nivoslider_effect = schema.Choice(
        title=_(u"label_nivoslider_effect", default=u"Transition Effect"),
        default='random',
        vocabulary=SimpleVocabulary([
            SimpleTerm('fold', 'fold',
                _(u"label_nivoslider_effect1", default=u"Fold")),
            SimpleTerm('fade', 'fade',
                _(u"label_nivoslider_effect2", default=u"Fade")),
            SimpleTerm('sliceDown', 'sliceDown',
                _(u"label_nivoslider_effect3", default=u"Slice Down")),
            SimpleTerm('sliceDownLeft', 'sliceDownLeft',
                _(u"label_nivoslider_effect16", default=u"Slice Down Left")),
            SimpleTerm('sliceUp', 'sliceUp',
                _(u"label_nivoslider_effect4", default=u"Slice Up")),
            SimpleTerm('sliceUpLeft', 'sliceUpLeft',
                _(u"label_nivoslider_effect5", default=u"Slice Up Left")),
            SimpleTerm('sliceUpDown', 'sliceUpDown',
                _(u"label_nivoslider_effect6", default=u"Slice Up Down")),
            SimpleTerm('sliceUpDownLeft', 'sliceUpDownLeft',
                _(u"label_nivoslider_effect7", default=u"Slice Up Down Left")),
            SimpleTerm('sliceInRight', 'sliceInRight',
                _(u"label_nivoslider_effect8", default=u"Slide In Right")),
            SimpleTerm('slideInLeft', 'slideInLeft',
                _(u"label_nivoslider_effect9", default=u"Slide In Left")),
            SimpleTerm('boxRain', 'boxRain',
                _(u"label_nivoslider_effect10", default=u"Box Rain")),
            SimpleTerm('boxRainReverse', 'boxRainReverse',
                _(u"label_nivoslider_effect11", default=u"Box Rain Reverse")),
            SimpleTerm('boxRandom', 'boxRandom',
                _(u"label_nivoslider_effect12", default=u"Box Random")),
            SimpleTerm('boxRainGrow', 'boxRainGrow',
                _(u"label_nivoslider_effect13", default=u"Box Rain Grow")),
            SimpleTerm('boxRainGrowReverse', 'boxRainGrowReverse',
                _(u"label_nivoslider_effect14",
                        default=u"box Rain Grow Reverse")),
            SimpleTerm('random', 'random',
                _(u"label_nivoslider_effect15", default=u"Random")
            )
        ]))
    nivoslider_randomstart = schema.Bool(
        title=_(u"label_nivoslider_randomstart",
            default=u"Start on random image?"),
        default=False)
    nivoslider_directionnav = schema.Bool(
        title=_(u"label_nivoslider_r_directionnar",
            default=u"Next & Prev navigation??"),
        default=False)
    nivoslider_directionnavhide = schema.Bool(
        title=_(u"label_nivoslider_directionnavhide",
            default=u"Only show Next & Prev on hover"),
        default=True)
    nivoslider_pauseonhover = schema.Bool(
        title=_(u"label_nivoslider_pauseonhover",
            default=u"Stop animation while hovering?"),
        default=False)
    nivoslider_slices = schema.Int(
        title=_(u"label_nivoslider_slices",
            default=u"Nuber of slices, for slice animations"),
        default=15)
    nivoslider_boxcols = schema.Int(
        title=_(u"label_nivoslider_boxcols",
            default=u"Number of columns for box animations"),
        default=8)
    nivoslider_boxrows = schema.Int(
        title=_(u"label_nivoslider_boxrows",
            default=u"Number of rows for box animations"),
        default=4)


class NivosliderDisplayType(BatchingDisplayType):

    name = u"nivoslider"
    schema = INivosliderDisplaySettings
    description = _(u"label_nivoslider_display_type",
        default=u"Nivoslider")

    def javascript(self):
        return u"""
<script type="text/javascript"
src="%(portal_url)s/++resource++ptg.nivoslider/js/jquery.nivo.slider.pack.js">
</script>
<script type="text/javascript">
$(window).load(function() {
    $('#slider').nivoSlider({
        effect: '%(effect)s', // Specify sets like: 'fold,fade,sliceDown'
        slices: %(slices)i, // For slice animations
        boxCols: %(boxcols)i, // For box animations
        boxRows: %(boxrows)i, // For box animations
        animSpeed: %(animspeed)i, // Slide transition speed
        pauseTime: %(delay)i, // How long each slide will show
        directionNav: %(directionnav)s, // Next & Prev navigation
        directionNavHide: %(directionnavhide)s, // Only show on hover
        controlNav: true, // 1,2,3... navigation
        controlNavThumbs: true, // Use thumbnails for Control Nav
        controlNavThumbsFromRel: true, // Use image rel for thumbs
        pauseOnHover: %(pauseonhover)s, // Stop animation while hovering
        randomStart: %(randomstart)s // Start on a random slide
    });
});
</script>
""" % {
         'portal_url': self.portal_url,
         'height': self.height,
         'effect': self.settings.nivoslider_effect,
         'slices': self.settings.nivoslider_slices,
         'boxcols': self.settings.nivoslider_boxcols,
         'boxrows': self.settings.nivoslider_boxrows,
         'animspeed': self.settings.duration,
         'delay': self.settings.delay,
         'directionnav': jsbool(self.settings.nivoslider_directionnav),
         'directionnavhide': jsbool(self.settings.nivoslider_directionnavhide),
         'pauseonhover': jsbool(self.settings.nivoslider_pauseonhover),
         'randomstart': jsbool(self.settings.nivoslider_randomstart)
    }

    def css(self):
        # for backwards compatibility.
        base_url = '%s/++resource++ptg.nivoslider' % (
            self.portal_url)
        return u"""
        <style>
        .nivoSlider {
        height: %(height)ipx !important;
        width: %(width)ipx !important;
        }
        div.slider-wrapper  {
        height: %(imageheight)ipx;
        width: %(imagewidth)ipx;
        }
        a.nivo-imageLink {
        height: 200px;
        }
        .ribbon {
        height: %(height)ipx;
        }
        </style>
<link rel="stylesheet" type="text/css" href="%(base_url)s/css/nivoslider.css"/>
<link rel="stylesheet" type="text/css"
    href="%(base_url)s/css/%(nivoslider_theme)s/style.css"/>
""" % {
        'height': self.settings.nivoslider_height,
        'width': self.settings.nivoslider_width,
        'imageheight': self.settings.nivoslider_height + 50,
        'imagewidth': self.settings.nivoslider_width + 40,
        'nivoslider_theme': self.settings.nivoslider_theme,
        'base_url': base_url
       }
NivosliderSettings = createSettingsFactory(NivosliderDisplayType.schema)