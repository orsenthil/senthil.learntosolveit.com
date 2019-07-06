.. title: Terraform Provider Dominos
.. slug: terraform-provider-dominos
.. date: 2019-07-05 21:47:46 UTC-07:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

I ordered Pizza using `terraform`_ today. I was learning about terraform and how provider can be anything,
even Software as a Service, which is basically an API.

So, it made possible to develop software like terraform-provider-dominos_ using which you can order Pizza.
I tried it. The terraform apply crashed for me, but I knew that terraform might have attempted the purchase operation
and had probably crashed due to slow response from the API.

It was the case, I saw my credit card charged in my account, an order confirmation email, and in 30 minutes, I got my pizza.

.. image:: https://dl.dropboxusercontent.com/s/wrwm5e74hxvultx/IMG_20190705_190646.jpg
   :width: 480
   :height: 350


.. _terraform: https://www.terraform.io/

.. _terraform-provider-dominos: https://github.com/ndmckinley/terraform-provider-dominos

