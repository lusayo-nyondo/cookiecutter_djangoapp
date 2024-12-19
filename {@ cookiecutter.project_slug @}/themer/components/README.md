# Components library

This is my base components library. I'm going to follow two general guidelines for
my components. All component context data and its validation will be handled via mixins.

As far as the library is concerned, context data will strictly be used for defining
the visibility of slots. This is expected to be handled within the templates.

I think the philosophy will generally be each template will provide the following:

    1. Text Properties that you can use to slot in simple text for components.
    2. Component slots that you can fill with your own HTML. You are entirely responsible for formatting them.

