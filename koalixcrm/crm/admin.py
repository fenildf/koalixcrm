# -*- coding: utf-8 -*-

from django.contrib import admin
from koalixcrm.crm.documents.quote import Quote, OptionQuote
from koalixcrm.crm.documents.purchase_confirmation import PurchaseConfirmation, OptionPurchaseConfirmation
from koalixcrm.crm.documents.delivery_note import DeliveryNote, OptionDeliveryNote
from koalixcrm.crm.documents.invoice import Invoice, OptionInvoice
from koalixcrm.crm.documents.payment_reminder import PaymentReminder, OptionPaymentReminder
from koalixcrm.crm.documents.purchase_order import PurchaseOrder, OptionPurchaseOrder
from koalixcrm.crm.documents.contract import Contract, OptionContract
from koalixcrm.crm.product.tax import Tax, OptionTax
from koalixcrm.crm.product.unit import Unit, OptionUnit
from koalixcrm.crm.product.product import Product, OptionProduct
from koalixcrm.crm.product.currency import Currency, OptionCurrency
from koalixcrm.crm.contact.customer import Customer, OptionCustomer
from koalixcrm.crm.contact.supplier import Supplier, OptionSupplier
from koalixcrm.crm.contact.customer_group import CustomerGroup, OptionCustomerGroup
from koalixcrm.crm.contact.customerbillingcycle import CustomerBillingCycle, OptionCustomerBillingCycle
from koalixcrm.crm.contact.person import Person
from koalixcrm.crm.contact.contact import OptionPerson, CallForContact, VisitForContact
from koalixcrm.crm.contact.call import OptionCall, OptionVisit
from koalixcrm.crm.reporting.task import Task, OptionTask
from koalixcrm.crm.reporting.task_link_type import TaskLinkType, OptionTaskLinkType
from koalixcrm.crm.reporting.task_status import TaskStatus, OptionTaskStatus
from koalixcrm.crm.reporting.project import Project, OptionProject
from koalixcrm.crm.reporting.project_link_type import ProjectLinkType, OptionProjectLinkType
from koalixcrm.crm.reporting.project_status import ProjectStatus, OptionProjectStatus
from koalixcrm.crm.reporting.work import Work, OptionWork
from koalixcrm.crm.reporting.reporting_period import ReportingPeriod, ReportingPeriodAdmin
from koalixcrm.crm.reporting.reporting_period_status import ReportingPeriodStatus, OptionReportingPeriodStatus


admin.site.register(Customer, OptionCustomer)
admin.site.register(CustomerGroup, OptionCustomerGroup)
admin.site.register(CustomerBillingCycle, OptionCustomerBillingCycle)
admin.site.register(Supplier, OptionSupplier)
admin.site.register(Person, OptionPerson)
admin.site.register(CallForContact, OptionCall)
admin.site.register(VisitForContact, OptionVisit)

admin.site.register(Contract, OptionContract)
admin.site.register(Quote, OptionQuote)
admin.site.register(PurchaseConfirmation, OptionPurchaseConfirmation)
admin.site.register(DeliveryNote, OptionDeliveryNote)
admin.site.register(Invoice, OptionInvoice)
admin.site.register(PaymentReminder, OptionPaymentReminder)
admin.site.register(PurchaseOrder, OptionPurchaseOrder)

admin.site.register(Unit, OptionUnit)
admin.site.register(Currency, OptionCurrency)
admin.site.register(Tax, OptionTax)
admin.site.register(Product, OptionProduct)

admin.site.register(Task, OptionTask)
admin.site.register(TaskLinkType, OptionTaskLinkType)
admin.site.register(TaskStatus, OptionTaskStatus)
admin.site.register(Work, OptionWork)
admin.site.register(Project, OptionProject)
admin.site.register(ProjectLinkType, OptionProjectLinkType)
admin.site.register(ProjectStatus, OptionProjectStatus)
admin.site.register(ReportingPeriod, ReportingPeriodAdmin)
admin.site.register(ReportingPeriodStatus, OptionReportingPeriodStatus)
