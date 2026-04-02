trigger BillingRecordCreation on Banquet_Hall__c (after insert) {
   if(trigger.isInsert){
        if(trigger.isAfter){
            BillingTriggerHandlerClass.BillingCreationonBooking(trigger.new);
        }
    }
}
